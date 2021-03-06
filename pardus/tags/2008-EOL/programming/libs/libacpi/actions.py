#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.export("CC", get.CC())
    shelltools.export("CFLAGS", get.CFLAGS())
    autotools.make()

def install():
    autotools.install("DESTDIR=%s PREFIX=/usr" % get.installDIR())

    pisitools.remove("/usr/lib/libacpi.a")
    pisitools.removeDir("/usr/share/doc/libacpi")

    pisitools.dohtml("doc/html/*")

    pisitools.dodoc("AUTHORS", "CHANGES", "LICENSE", "README", "TODO")
