#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-208 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("lsusb.8", "/usr/share/usb.ids", "/usr/share/misc/usb.ids")

    autotools.autoreconf("-fi")
    autotools.configure("--datadir=/usr/share/misc \
                         --disable-zlib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
