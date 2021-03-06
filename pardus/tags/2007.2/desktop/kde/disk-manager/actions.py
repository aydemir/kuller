#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005-2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def install():
    pythonmodules.install()
    binpath = "%s/bin/disk-manager" % get.kdeDIR()
    pisitools.remove(binpath)
    pisitools.dosym("%s/share/apps/disk-manager/disk-manager.py" % get.kdeDIR(), binpath)

