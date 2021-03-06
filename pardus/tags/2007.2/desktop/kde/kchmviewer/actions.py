#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    kde.configure("--with-kde")

def build():
    kde.make()

def install():
    kde.install()
    pisitools.remove("/usr/kde/3.5/share/applnk/kchmviewer.desktop")
    pisitools.domo("po/tr.po", "tr", "kchmviewer.mo")
