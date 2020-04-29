#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

def setup():
    # fix ImportError: /usr/lib/python3.8/site-packages/yara_python-4.0.0-py3.8-linux-x86_64.egg/yara.cpython-38-x86_64-linux-gnu.so: undefined symbol: yr_finalize
    pisitools.dosed("setup.py", "include_dirs=\['yara/libyara/include', 'yara/libyara/', '.", "libraries = ['yara")

def build():
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-discarded-qualifiers -Wno-sign-compare")
    # fix unused direct dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread -lbz2")
    pythonmodules.compile(pyVer="3")
    
#def check():
#    pythonmodules.compile("test", pyVer="3")

def install():
    pythonmodules.install(pyVer="3")