#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="bully-1.4-00" + "/src/"

def build():
    pisitools.cflags.add("-Wno-implicit-function-declaration")
    autotools.make()

def install():
    pisitools.dobin("bully")
    #pisitools.dodoc("LICENSE*", "README*")