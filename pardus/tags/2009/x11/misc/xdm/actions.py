#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")

    autotools.configure("--disable-static \
                         --enable-unix-transport \
                         --enable-tcp-transport \
                         --enable-IPv6 \
                         --enable-local-transport \
                         --enable-secure-rpc \
                         --enable-xpm-logos \
                         --enable-dynamic-greeter \
                         --enable-xdm-auth \
                         --with-pam \
                         --with-xdmconfigdir=/etc/X11/xdm \
                         --with-default-vt=vt7 \
                         --with-config-type=ws \
                         --with-xft \
                         --with-pixmapdir=/usr/share/X11/xdm/pixmaps")

    # Put flags in front of the libs. Needed for --as-needed.
    replace = (r"(\\\$deplibs) (\\\$compiler_flags)", r"\2 \1")
    pisitools.dosed("libtool", *replace)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/lib/xdm")

    pisitools.dodoc("AUTHORS", "COPYING", "README")