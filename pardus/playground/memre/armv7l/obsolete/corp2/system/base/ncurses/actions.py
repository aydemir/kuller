#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ncurses-%s" % get.srcVERSION().split("_", 1)[0]

def setup():
    pisitools.dosed("progs/Makefile.in", r"(^transform\s*=).*$", r"\1")
    crosstools.configure("--without-debug \
                          --without-profile \
                          --disable-rpath \
                          --enable-const \
                          --enable-largefile \
                          --enable-widec \
                          --with-terminfo-dirs='/etc/terminfo:/usr/share/terminfo' \
                          --disable-termcap \
                          --with-shared \
                          --with-rcs-ids \
                          --with-chtype='long' \
                          --with-mmask-t='long' \
                          --without-ada \
                          --enable-symlinks \
                          --with-manpage-format=normal \
                          --with-build-cc=\"gcc -D_GNU_SOURCE\" \
                          --enable-widec")

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("program_transform_name= DESTDIR=%s" % get.installDIR())

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    for file in shelltools.ls(get.installDIR() + "/usr/lib/*w.*"):
        source = file.replace(get.installDIR(), "")
        destination = source.replace("w.", ".")
        pisitools.dosym(source.replace("/usr/lib/", ""), destination)

    for file in shelltools.ls(get.installDIR() + "/lib/libncursesw.so*"):
        source = file.replace(get.installDIR(), "")
        destination = source.replace("w.", ".")
        pisitools.dosym(source.replace("/usr/lib/", ""), destination)

    # We need the basic terminfo files in /etc
    terminfo = ["ansi", "console", "dumb", "linux", "rxvt", "screen", "sun", \
                "vt52", "vt100", "vt102", "vt200", "vt220", "xterm", "xterm-color", "xterm-xfree86"]

    for file in terminfo:
        termfile = file[0] + "/" + file
        if shelltools.can_access_file("/usr/share/terminfo/%s" % termfile):
            pisitools.dodir("/etc/terminfo/%s" % file[0])
            pisitools.domove("/usr/share/terminfo/%s" % termfile, "/etc/terminfo/%s" % file[0])
            pisitools.dosym("../../../../etc/terminfo/%s/%s" % (file[0], file ), "/usr/share/terminfo/%s/%s" % (file[0], file ))

    pisitools.dodoc("ANNOUNCE", "NEWS", "README*", "TO-DO")
