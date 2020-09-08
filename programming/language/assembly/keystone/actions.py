#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build-shared")
    shelltools.makedirs("build-static")
    shelltools.cd("build-shared")
    cmaketools.configure("-DCMAKE_SKIP_RPATH=ON \
                          -DBUILD_SHARED_LIBS=ON \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DLLVM_TARGETS_TO_BUILD=all \
                          -G 'Unix Makefiles'", sourceDir="..")
    
    shelltools.cd("../build-static")
    cmaketools.configure("-DCMAKE_SKIP_RPATH=ON \
                          -DBUILD_SHARED_LIBS=OFF \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DLLVM_TARGETS_TO_BUILD=all \
                          -G 'Unix Makefiles'", sourceDir="..")

def build():
    shelltools.cd("build-shared")
    cmaketools.make()
    shelltools.cd("../build-static")
    cmaketools.make()

def install():
    shelltools.cd("build-shared")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../build-static")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # add license
    shelltools.cd("..")
    pisitools.dodoc("COPYING*", "LICENSE*", "README*")
    # add samples
    pisitools.insinto("/usr/share/doc/keystone/samples", "samples/*")