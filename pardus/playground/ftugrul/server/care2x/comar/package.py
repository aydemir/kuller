#!/usr/bin/python

import os

def postInstall():

    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/cache")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/cache/barcodes")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/counter")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/counter/hitcount.txt")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/fotos")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/fotos/encounter")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/fotos/registration")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/fotos/news")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/logs")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/logs/access")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/logs/access/2006")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/logs/access_fail")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/logs/access_fail/2006")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/pharma")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/pharma/img")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/med_depot")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/med_depot/img")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/radiology")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/radiology/dicom_img")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/gui")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/gui/img")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/gui/img/logos_dept")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/gui/smarty_template/templates_c")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/include")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/include/inc_init_main.php")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/installer")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x/installer/install.php")
    os.system("/usr/bin/chmod 777 /var/www/localhost/htdocs/care2x")
    os.system("/usr/bin/chmod -R 777 /var/www/localhost/htdocs/care2x/gui/smarty_template/templates_c/default")