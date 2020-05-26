#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="ADMIDpack" + "/src/"

def setup():
    pisitools.dosed("Makefile", " -lpcap", " -Wl,-O1,--as-needed -lpcap ")

def build():
    shelltools.system('make CC="gcc $CFLAGS -Wno-unused-result -Wno-int-to-pointer-cast -Wno-implicit-function-declaration"')

def install():
    pisitools.dobin("../ADMbin/ADM*")
    pisitools.insinto("/usr/share/doc/admid-pack", "../Docs/*")