#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-fi")
    autotools.configure()

    # Drop unused deps
    #pisitools.dosed("src/Makefile", "^recordmydesktop_LDFLAGS = .*$", "recordmydesktop_LDFLAGS = ")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
