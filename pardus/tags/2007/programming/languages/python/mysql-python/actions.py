#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules

WorkDir = "MySQL-python-1.2.1c8"

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
