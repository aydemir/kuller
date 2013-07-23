#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Tk-%s" % get.srcVERSION()

def setup():
    perlmodules.configure("X11INC=/usr/include/X11/ X11LIB=/usr/lib/X11/ ")

def build():
    perlmodules.make()

def install():
    perlmodules.install()
    pisitools.dodoc("Changes", "README")