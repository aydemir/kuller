#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def build():
    autotools.make("KERN_DIR=/lib/modules/%s/build" % get.curKERNEL())

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")
