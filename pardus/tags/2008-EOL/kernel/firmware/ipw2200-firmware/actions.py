#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "ipw2200-fw-3.0"

def install():
    pisitools.insinto("/lib/firmware", "*.fw")
    pisitools.insinto("/lib/firmware", "LICENSE", "ipw-2.4-LICENSE")
