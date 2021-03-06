#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-pcm-plugins=all \
                         --with-ctl-plugins=all \
                         --with-versioned \
                         --with-libdl \
                         --with-pthread \
                         --with-librt \
                         --enable-shared \
                         --enable-python")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "TODO", "COPYING", "doc/*.txt")
