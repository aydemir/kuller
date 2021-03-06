#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    kde.make("-f admin/Makefile.common")
    kde.configure("--with-xine \
                   --with-gstreamer")

def build():
    kde.make()

def install():
    kde.install()

    pisitools.remove("%s/share/mimelnk/application/x-mplayer2.desktop" % get.kdeDIR())
