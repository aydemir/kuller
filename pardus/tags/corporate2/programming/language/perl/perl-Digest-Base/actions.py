#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Digest-%s" % get.srcVERSION()

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.removeDir("/usr/lib/perl5/vendor_perl/%s/%s-linux-thread-multi/" % (get.curPERL(), get.ARCH()))
    pisitools.dodoc("README","Changes")
