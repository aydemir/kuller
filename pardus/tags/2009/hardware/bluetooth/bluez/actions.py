#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():

    # Fix udev paths
    pisitools.dosed("scripts/bluetooth-serial.rules", "bluetooth_serial", "/lib/udev/bluetooth_serial")
    pisitools.dosed("scripts/Makefile.am", "^rulesdir = .*$", "rulesdir = /lib/udev/rules.d")

    autotools.autoreconf("-fi")

    autotools.configure("--enable-network \
                         --enable-serial \
                         --enable-input \
                         --enable-audio \
                         --enable-service \
                         --enable-gstreamer \
                         --enable-alsa \
                         --enable-usb \
                         --enable-netlink \
                         --enable-tools \
                         --enable-bccmd \
                         --enable-hid2hci \
                         --enable-dfutool \
                         --enable-cups \
                         --enable-hidd \
                         --enable-dund \
                         --enable-pand \
                         --enable-test \
                         --enable-manpages \
                         --enable-configfiles \
                         --disable-pcmciarules \
                         --disable-initscripts \
                         --with-html-dir=%s/%s/html \
                         --localstatedir=/var" % (get.docDIR(), get.srcNAME()))
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("-C tools/ DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("-C test/ DESTDIR=%s" % get.installDIR())

    # Install oui file
    pisitools.insinto("/usr/share/misc", "oui.txt")

    # Install shipped udev for serial PCMCIA devices
    pisitools.insinto("/lib/udev/rules.d", "scripts/bluetooth-serial.rules", "97-bluetooth-pcmcia.rules")

    # Install shipped udev script
    pisitools.dobin("scripts/bluetooth_serial", "/lib/udev")

    # Install conf files
    for i in ["audio", "input", "network"]:
        pisitools.insinto("/etc/bluetooth", "%s/%s.conf" % (i,i))

    # Simple test tools
    for i in ["simple-agent", "simple-service", "monitor-bluetooth",
              "list-devices", "apitest", "hsmicro", "hsplay",
              "test-adapter", "test-device", "test-discovery",
              "test-manager", "test-serial", "test-service",
              "test-telephony", "hstest", "attest", "sdptest",
              "scotest"]:
        pisitools.dobin("test/%s" % i)

    # Additional tools
    pisitools.dosbin("tools/hcisecfilter")
    pisitools.dosbin("tools/ppporc")

    # Install documents
    pisitools.dodoc("AUTHORS", "ChangeLog", "README")
