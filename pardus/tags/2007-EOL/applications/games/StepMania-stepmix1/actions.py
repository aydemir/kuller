#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

WorkDir = "."
NoStrip = "/"

def install():
    pisitools.insinto("/usr/share/StepMania/Songs", "Songs/*")
    pisitools.insinto("/usr/share/StepMania/Songs", "smzip.ctl")