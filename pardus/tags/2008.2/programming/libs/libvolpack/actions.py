#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "volpack-%s" % get.srcVERSION().replace("_pre7","c7")

def setup():
    shelltools.export("CXXFLAGS", get.CXXFLAGS())
    shelltools.export("CFLAGS", get.CFLAGS())
    autotools.configure("--enable-static=no")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "todo")

    #add examples
    pisitools.dodir("%s/%s/examples" % (get.docDIR(), get.srcTAG()))
    pisitools.insinto("%s/%s/examples" % (get.docDIR(), get.srcTAG()), "examples/.libs/*")
    pisitools.insinto("%s/%s/examples" % (get.docDIR(), get.srcTAG()), "examples/brainsmall.den")
