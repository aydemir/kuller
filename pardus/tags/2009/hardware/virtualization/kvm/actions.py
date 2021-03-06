#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


NoStrip=["/usr/share/kvm"]
WorkDir="qemu-kvm-devel-%s" % get.srcVERSION()

cflags = get.CFLAGS().replace("-fpie", "").replace("-fstack-protector", "")

def setup():
    shelltools.sym("asm-x86", "kernel/include/asm")
    shelltools.export("CFLAGS", cflags)
    autotools.rawConfigure('--prefix=/usr \
                            --disable-werror \
                            --audio-drv-list="alsa pa" \
                            --cc="%s" \
                            --host-cc="%s" \
                            --enable-system \
                            --enable-linux-user \
                            --disable-bsd-user \
                            --disable-darwin-user' % (get.CC(), get.CC()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/bin/qemu-system-x86_64", "/usr/bin/", "qemu-kvm")
    pisitools.domove("/usr/share/man/man1/qemu.1", "/usr/share/man/man1/", "qemu-kvm.1")

    # Use the one qemu provides
    pisitools.remove("/usr/bin/qemu-img")
    pisitools.remove("/usr/share/man/man1/qemu-img.1")
    pisitools.remove("/usr/bin/qemu-nbd")
    pisitools.remove("/usr/share/man/man8/qemu-nbd.8")
    pisitools.removeDir("/usr/share/doc")
