#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools

def setup():

    autotools.configure("--with-alsa \
                         --with-faac \
                         --with-vorbis \
                         --with-lame \
                         --without-jack")
def build():

    autotools.make()
def install():

    autotools.install()
