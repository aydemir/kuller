#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.removeDir("/usr/share/doc")
    pisitools.dodoc("ChangeLog", "COPYING", "README", "AUTHORS", "TODO")
    pisitools.dohtml("doc/html")
