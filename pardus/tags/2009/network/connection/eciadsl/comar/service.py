# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "EciADSL Daemon",
                 "tr": "EciADSL Servisi"})

@synchronized
def start():
    startService(command="/usr/bin/eciadsl-start",
                 pidfile="/var/run/ppp-eciadsl.pid",
                 donotify=True)

@synchronized
def stop():
    startService(command="/usr/bin/eciadsl-stop",
                 args="",
                 donotify=True)

def status():
    return isServiceRunning("/var/run/ppp-eciadsl.pid")
