#/usr/bin/python

import os

def postInstall():
    if os.path.exists("/usr/sbin/iconvconfig"):
        # Generate fastloading iconv module configuration file.
        os.popen("/usr/sbin/iconvconfig --prefix=/")
    
    # Reload init ...
    os.popen("/sbin/init U &> /dev/null")

    # Nscd needs this to work
    os.popen("mkdir -p /var/run/nscd")
