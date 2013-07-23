#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools

def setup():
    crosstools.autoreconf("-vif")
    crosstools.configure()

def build():
    crosstools.make()

def install():
    crosstools.install()

    pisitools.dodoc("doc/*.txt", "COPYING", "NEWS", "README", "TODO")