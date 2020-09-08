#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

def build():
    shelltools.cd("bindings/python")
    pythonmodules.compile()

def install():
    shelltools.cd("bindings/python")
    pythonmodules.install()