#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import perlmodules
from pisi.actionsapi import autotools

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()
    autotools.make("samples")

def install():
    perlmodules.install()
