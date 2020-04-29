#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

def setup():
    # fix ImportError: ... undefined symbol: yr_finalize
    pisitools.dosed("setup.py", "include_dirs=\['yara/libyara/include', 'yara/libyara/', '.", "libraries = ['yara")

def build():
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-discarded-qualifiers -Wno-sign-compare")
    # fix unused direct dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread")
    pythonmodules.compile()
    
#def check():
#    pythonmodules.compile("test")

def install():
    pythonmodules.install()