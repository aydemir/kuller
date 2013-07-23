#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir="libxml++-%s" % get.srcVERSION()

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make("-j1")

def install():
    autotools.install()
