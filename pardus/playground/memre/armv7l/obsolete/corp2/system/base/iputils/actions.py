#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="iputils-s%s" % get.srcVERSION()

def build():
    crosstools.make()

def install():
    for app in ["ping","ping6"]:
        pisitools.dobin(app)

    for app in ["clockdiff","arping","rdisc","tracepath","tracepath6","traceroute6"]:
        pisitools.dosbin(app)

    shelltools.chmod("%s/usr/bin/ping" % get.installDIR(), 04711)
    shelltools.chmod("%s/usr/bin/ping6" % get.installDIR(), 04711)

    pisitools.dodoc("RELNOTES")