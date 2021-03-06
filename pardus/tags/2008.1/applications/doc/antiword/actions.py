#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile","-O2",get.CFLAGS())

def build():
    autotools.make()

def install():
    pisitools.dobin("antiword")

    pisitools.insinto("/usr/share/antiword","Resources/*")
    pisitools.chmod("%s/usr/share/antiword/*" % get.installDIR(), 0644)

    pisitools.doman("Docs/antiword.1")
    pisitools.dodoc("Docs/COPYING","Docs/ChangeLog","Docs/FAQ","Docs/Emacs","Docs/Mutt","Docs/ReadMe","Docs/QandA")
