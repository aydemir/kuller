#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools

WorkDir="dvdrip-%s" % get.srcVERSION()

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()
    pisitools.insinto("/usr/share/applications/", "dvdrip.desktop")
    pisitools.insinto("/usr/share/pixmaps/", "lib/Video/DVDRip/icon.xpm", "dvdrip.xpm")
    pisitools.dodoc("Changes", "Changes.0.46", "Credits", "README", "TODO")