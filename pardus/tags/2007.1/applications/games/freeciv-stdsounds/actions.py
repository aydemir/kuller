#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get 

WorkDir = "data"

def install():
    pisitools.dodir("/usr/share")
    shelltools.cd("..")
    shelltools.copytree("data", "%s/usr/share/freeciv" % get.installDIR())
