#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.unlinkDir("libltdl")
    libtools.libtoolize("-c -f --ltdl")
    autotools.autoreconf("-fi")

    autotools.configure("--sysconfdir=/etc/unixODBC \
                         --enable-gui=no \
                         --disable-stats \
                         --x-libraries=/usr/lib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
    pisitools.dohtml("doc/*")
