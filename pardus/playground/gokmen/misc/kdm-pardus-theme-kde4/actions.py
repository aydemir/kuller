#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
WorkDir = "kdm-pardus-theme-kde4"

def install():
    pisitools.insinto("/usr/kde/4/share/apps/kdm/themes/pardus/", "./*")
