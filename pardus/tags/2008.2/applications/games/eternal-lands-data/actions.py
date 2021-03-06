#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

#WorkDir = "./"
#packdir = "el_install"
WorkDir = "el_install"

datadir = "/usr/share/eternal-lands"
NoStrip = ["/usr/share/eternal-lands"]

data = ["2dobjects", "3dobjects", "actor_defs", "animations", "languages", "mapeditor",
        "maps", "meshes", "particles", "shaders", "skeletons","skybox", "sound", "textures", "tiles"]


def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

#def setup():
#    shelltools.chmod(packdir, 0755)
#    fixperms(packdir)

def install():
    # shelltools.cd(packdir)

    for files in ["3dobjects.txt", "e3dlist.txt", "global_filters.txt", "sound_warnings.txt",
                  "*.lst", "*.xml", "*.cfg"]:
        pisitools.insinto(datadir, files)

    for f in data:
        shelltools.copytree(f, "%s/%s" % (get.installDIR(), datadir))

    fixperms(get.installDIR())

    pisitools.dohtml("*.html")
    pisitools.dodoc("license.txt")
