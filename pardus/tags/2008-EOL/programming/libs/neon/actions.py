#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-xml2 \
                         --with-ssl \
                         --with-zlib \
                         --without-gssapi \
                         --with-ssl=openssl \
                         --enable-threadsafe-ssl=posix \
                         --enable-shared \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("THANKS", "TODO", "ChangeLog", "AUTHORS", "BUGS", "NEWS", "README", "doc/*")
