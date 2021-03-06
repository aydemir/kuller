#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="ndiswrapper-%s" % get.srcVERSION()

def build():
    pisitools.dosed("driver/Makefile", "/misc", "/extra")
    autotools.make("-C /lib/modules/%s/build M=`pwd`" % get.curKERNEL())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/lib/modules/%s/modules*" % get.curKERNEL())
    pisitools.dodir("/etc/ndiswrapper")

    pisitools.dodoc("README", "AUTHORS", "ChangeLog")
