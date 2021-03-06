#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="SDL_Perl-%s" % get.srcVERSION()

perlautodir = "/usr/lib/perl5/vendor_perl/%s/i686-linux-thread-multi/auto" % get.curPERL()

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()

    pisitools.domove("%s/src/*" % perlautodir,"%s/" % perlautodir)
    pisitools.removeDir("%s/src/" % perlautodir)

    pisitools.dodoc("README","CHANGELOG")
