#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

NoStrip = "/"

data = ["BackgroundEffects", "BackgroundTransitions", "BGAnimations",
        "Characters", "Courses", "Data", "NoteSkins", "Themes"]
datadir = "/usr/share/StepMania"

def install():
    pisitools.dodir(datadir)

    for i in data:
        shelltools.copytree(i, "%s/%s" % (get.installDIR(), datadir))
