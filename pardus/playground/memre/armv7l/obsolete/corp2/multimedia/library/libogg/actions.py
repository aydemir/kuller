#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("doc/Makefile.in", "^docdir = .*$", "docdir = $(datadir)/doc/$(PACKAGE)")
    pisitools.dosed("doc/libogg/Makefile.in", "^docdir = .*$", "docdir = $(datadir)/doc/$(PACKAGE)/ogg")

    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "CHANGES", "COPYING", "README")
