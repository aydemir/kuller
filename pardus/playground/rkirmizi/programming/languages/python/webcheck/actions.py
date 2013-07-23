#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/lib/python2.4/site-packages/webcheck", "*")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "HACKING", "NEWS", "README", "TODO")
