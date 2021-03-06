#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system('../mozilla/nsprpub/configure \
                       --prefix=/usr \
                       --disable-debug \
                       --enable-optimize="%s -g -fno-strict-aliasing"' % get.CFLAGS())

def build():
    shelltools.cd("build")
    autotools.make()

def install():
    shelltools.cd("build")

    pisitools.insinto("/usr/lib","dist/lib/*.so",sym=False)
    pisitools.insinto("/usr/include/nspr","dist/include/nspr/*.h",sym=False)
    pisitools.insinto("/usr/include/nspr/obsolete","dist/include/nspr/obsolete/*.h",sym=False)
    pisitools.insinto("/usr/include/nspr/private","dist/include/nspr/private/*.h",sym=False)

    pisitools.insinto("/usr/bin","config/nspr-config",sym=False)
    pisitools.insinto("/usr/lib/pkgconfig","config/nspr.pc",sym=False)
