#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "sauerbraten"
data = "/usr/share/sauerbraten"
docdir = "%s/%s" % (get.docDIR(), get.srcNAME())

# workaround for bug #6304 for now
NoStrip = ["/usr/share/sauerbraten/packages"]

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
            if name == "CVS":
                shelltools.unlinkDir(os.path.join(root, name))
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)


def setup():
    shelltools.cd("src")
    pisitools.dosed("Makefile", "^CXX=.*", "CXX=%s" % get.CXX())
    pisitools.dosed("Makefile", "^CXXOPTFLAGS=.*", "CXXOPTFLAGS=%s" % get.CXXFLAGS())
    pisitools.dosed("Makefile", "strip", "# strip")

def build():
    shelltools.cd("src")
    autotools.make("-j1 all")

def install():
    pisitools.dodir("%s/bin_unix" % data)

    for f in ["sauer_client", "sauer_server"]:
        pisitools.dobin("src/%s" % f, "%s/bin_unix" % data)

    for d in ["data", "packages", "docs"]:
        fixperms(d)

    for d in ["data", "packages"]:
        pisitools.insinto(data, d)

    pisitools.dodir(docdir)
    pisitools.insinto(docdir, "docs/*")

