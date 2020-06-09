#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    # suppress compiler warnings
    pisitools.dosed("Makefile", "CFLAGS = -W -g3", "CFLAGS = -W -g3 -Wno-implicit-function-declaration -Wno-incompatible-pointer-types")
    autotools.make()

def install():
    # no install rule:
    pisitools.dobin("bluesnarfer")
    pisitools.dodoc("README")
