#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("Makefile","PREFIX=/usr/local","PREFIX=/usr")

def build():
    autotools.make()

def install():
    docdir = "%s/%s/%s" % (get.installDIR(), get.docDIR(), get.srcTAG())
    autotools.rawInstall("PKG_ROOT=%s DOC_PREFIX=%s" % (get.installDIR(), docdir))
    pisitools.remove("/usr/X11R6/include/X11/pixmaps/tuxpaint.xpm")
