#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    dict_path = "/usr/share/stardict/dic/stardict-freedict-tur-eng/"

    pisitools.dodir(dict_path)
    pisitools.insinto(dict_path, "*")
