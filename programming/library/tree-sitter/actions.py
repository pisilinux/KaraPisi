#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed("Makefile", "PREFIX \?= /usr/local", "PREFIX ?= /usr/")

def build():
    autotools.make()

    # FIXME
    # i couldn't build `tree-sitter.js` and `tree-sitter.wasm` using
    # the script below. i' ve got sandbox error.

    # for building commandline tools
    #shelltools.system("./script/build-wasm")
    shelltools.cd("cli")
    shelltools.system("cargo build --release --locked --all-features")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    # install executable manually:
    pisitools.dobin("target/release/tree-sitter")
    pisitools.dodoc("LICENSE", "README*")
    pisitools.insinto("/usr/share/doc/tree-sitter", "%s/%s/docs" % (get.workDIR(), get.srcNAME()+"-"+get.srcVERSION()))