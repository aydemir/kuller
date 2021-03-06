#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    pisitools.dosed("Makefile", "-Werror", "-D_GNU_SOURCE")
    autotools.make("INSTPREFIX=%s" % get.installDIR())

def install():
    pisitools.dodir("/usr/bin")
    autotools.rawInstall("INSTPREFIX=%s" % get.installDIR())

    pisitools.dodoc("Changelog", "README", "Changelog")
