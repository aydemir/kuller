#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "module-init-tools-3.3-pre11"

def setup():
    shelltools.export("WANT_AUTOMAKE", "1.6")

    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/ \
                         --enable-zlib")

def build():
    autotools.make()

def install():
    autotools.install("prefix=%s" % get.installDIR())
    pisitools.dosym("../bin/lsmod", "/sbin/lsmod")

    pisitools.dosbin("generate-modprobe.conf", "/sbin")
    pisitools.dodir("/etc")

    pisitools.doman("*.[1-8]")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
