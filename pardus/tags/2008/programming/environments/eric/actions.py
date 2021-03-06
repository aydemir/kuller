#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt


from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "eric4-%s" % get.srcVERSION()

conf = {"bindir": "/usr/bin",
        "installdir": get.installDIR(),
        "site-packages": "/usr/lib/%s/site-packages" % get.curPYTHON()}

def install():
    # make qt detection easy
    pisitools.dodir("/usr/qt/4")

    pythonmodules.run("install.py -z \
                                  -b %(bindir)s \
                                  -i %(installdir)s \
                                  -d %(site-packages)s \
                                  -c" % conf)

    pythonmodules.fixCompiledPy()

    pisitools.dodoc("ChangeLog", "LICENSE.GPL", "THANKS", "README*")
