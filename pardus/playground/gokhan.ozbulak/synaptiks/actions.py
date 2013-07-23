#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde4
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

# shelltools.export("HOME", get.workDIR())

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install("--single-version-externally-managed")