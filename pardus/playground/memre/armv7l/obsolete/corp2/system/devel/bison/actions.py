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

def setup():
    crosstools.configure("--enable-nls")

    shelltools.echo("config.h", "#define YYENABLE_NLS 1")

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/bin/yacc", "/usr/bin", "yacc.bison")
    pisitools.removeDir("/usr/lib/")

    pisitools.dodoc("AUTHORS", "NEWS", "ChangeLog", "README", "COPYING")
