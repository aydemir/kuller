#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().replace("_", "-"))

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodir("/lib/udev/rules.d")
    pisitools.domove("/etc/udev/rules.d/*.rules", "/lib/udev/rules.d")
    pisitools.removeDir("/etc/udev/rules.d")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "HACKING", "NEWS", "README", "THANKS", "TODO")
