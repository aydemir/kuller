#!/usr/bin/python

import os

def createNode(mode, uid, gid, minor, major, path):
    os.system("/usr/bin/mknod --mode=%d %s c %d %d" % (mode, path, minor, major))
    os.system("/usr/bin/chown %s:%s %s" % (uid, gid, path))

def postInstall():
    createNode(600, "root", "tty", 5, 1, "/lib/udev/devices/console")
    createNode(600, "root", "root" ,1, 11, "/lib/udev/devices/kmsg")
    createNode(666, "root", "root" ,1, 3, "/lib/udev/devices/null")
    createNode(666, "root", "root" ,1, 5, "/lib/udev/devices/zero")
    createNode(600, "root", "root" ,10, 135, "/lib/udev/devices/rtc")
    createNode(666, "root", "tty"  ,5, 2, "/lib/udev/devices/ptmx")
    createNode(666, "root", "tty"  ,5, 0, "/lib/udev/devices/tty")
    createNode(620, "root", "tty"  ,4, 1, "/lib/udev/devices/tty1")
    createNode(600, "root", "root" ,10, 130, "/lib/udev/devices/watchdog")
    createNode(600, "root", "dialout" ,108, 0, "/lib/udev/devices/ppp")
    createNode(600, "root", "root" ,10, 200, "/lib/udev/devices/net/tun")
    createNode(600, "root", "root" ,36, 0, "/lib/udev/devices/route")
    createNode(600, "root", "root" ,10, 200, "/lib/udev/devices/skip")

    try:
        os.symlink("/proc/self/fd", "/lib/udev/devices/fd")
    except OSError:
        pass

    try:
        os.symlink("/proc/self/fd/0", "/lib/udev/devices/stdin")
    except OSError:
        pass

    try:
        os.symlink("/proc/self/fd/1", "/lib/udev/devices/stdout")
    except OSError:
        pass

    try:
        os.symlink("/proc/self/fd/2", "/lib/udev/devices/stderr")
    except OSError:
        pass

    try:
        os.symlink("/proc/kcore", "/lib/udev/devices/core")
    except OSError:
        pass
