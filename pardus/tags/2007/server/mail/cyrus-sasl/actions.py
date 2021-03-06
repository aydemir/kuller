#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.remove("saslauthd/acinclude.m4")
    pisitools.remove("saslauthd/autom4te.cache")
    pisitools.remove("autom4te.cache")
    pisitools.remove("acinclude.m4")
    autotools.aclocal("-I cmulocal -I config")
    autotools.autoheader()
    autotools.autoconf()
    shelltools.cd("saslauthd")
    autotools.aclocal("-I ../cmulocal -I ../config")
    autotools.autoheader()
    autotools.autoconf()
    shelltools.cd("../")

    autotools.configure("--with-saslauthd=/var/lib/sasl2 \
                         --with-pwcheck=/var/lib/sasl2  \
                         --with-configdir=/etc/sasl2 \
                         --with-plugindir=/usr/lib/sasl2 \
                         --with-dbpath=/etc/sasl2/sasldb2 \
                         --enable-login \
                         --enable-ntlm \
                         --enable-auth-sasldb \
                         --disable-krb4 \
                         --disable-otp \
                         --disable-static \
                         --with-openssl \
                         --with-pam \
                         --with-ldap \
                         --disable-gssapi \
                         --without-mysql \
                         --disable-mysql \
                         --without-pgsql \
                         --disable-postgres \
                         --disable-java \
                         --disable-sql \
                         --with-devrandom=/dev/urandom \
                         --with-dblib=gdbm")

def build():
    autotools.make()
    shelltools.cd("saslauthd/")
    autotools.make("testsaslauthd")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodir("/etc/sasl2")
    pisitools.dodir("/var/lib/sasl2")

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README", "doc/TODO", "doc/*.txt")
    pisitools.dohtml("doc/*.html")

    for doc in ["AUTHORS", "COPYING", "ChangeLog", "LDAP_SASLAUTHD", "NEWS", "README"]:
        pisitools.newdoc("saslauthd/%s" % doc, "saslauthd/%s" % doc)
