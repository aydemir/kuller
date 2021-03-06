#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

builddir = "build/release-linux-i386"
datadir = "/usr/share/WoP"
NoStrip = "%s/wop" % datadir

def setup():
    pisitools.dosed("Makefile", "-O3", "%s -DUSE_ACTOR_DEFAULTS" % get.CFLAGS())
    pisitools.dosed("Makefile", "CC=gcc", "CC=%s" % get.CC())

def build():
    autotools.make("DEFAULT_BASEDIR=%s \
                    BUILD_SERVER=1 \
                    BUILD_CLIENT=1 \
                    BUILD_CLIENT_SMP=1 \
                    BUILD_GAME_SO=1 \
                    BUILD_GAME_QVM=1 \
                    USE_SDL=1 \
                    USE_OPENAL=1 \
                    USE_CODEC_VORBIS=1 \
                    USE_LOCAL_HEADERS=1" % (datadir))

def install():
    pisitools.dobin("build/release-linux-i386/wop-engine.i386")
    pisitools.dobin("build/release-linux-i386/wop-smp.i386")
    pisitools.dobin("build/release-linux-i386/wopded.i386")

    pisitools.rename("/usr/bin/wop-engine.i386", "WoP")
    pisitools.rename("/usr/bin/wop-smp.i386", "WoP-smp")
    pisitools.rename("/usr/bin/wopded.i386", "WoP-server")

    pisitools.doexe("%s/baseq3/*.so" % builddir, "%s/baseq3" % datadir)
    pisitools.insinto("%s/baseq3/vm/" % datadir, "%s/baseq3/vm/*" % builddir)

    pisitools.doexe("%s/missionpack/*.so" % builddir, "%s/missionpack" % datadir)
    pisitools.insinto("%s/missionpack/vm" % datadir, "%s/missionpack/vm/*" % builddir)

    pisitools.insinto("%s/wop" % datadir, "wop_patch_1_2/*.cfg")
    pisitools.insinto("%s/wop" % datadir, "wop_patch_1_2/*.pk3")

    pisitools.dodoc("BUGS", "ChangeLog", "*.txt", "wop_patch_1_2/*.txt", "NOTTODO", "TODO", "README")
