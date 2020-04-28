#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-stringop-overflow -Wno-strict-overflow -Wno-address-of-packed-member -Wno-stringop-truncation")
    autotools.autoreconf("-i")
    autotools.configure("--with-experimental")
    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()
    
def check():
    autotools.make("check")

def install():
    autotools.install("sqlite=true experimental=true pcre=true")
    pisitools.dodoc("LICENSE", "README")