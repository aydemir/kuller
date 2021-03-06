#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="4Suite-XML-%s" % get.srcVERSION()

def setup():
    pythonmodules.run("setup.py config --prefix=/usr \
                       --docdir=/usr/share/doc/%s" % get.srcTAG())

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("COPYRIGHT", "README", "docs/*")
