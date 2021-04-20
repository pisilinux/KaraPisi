#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools


def setup():
    # suppress compiler warnings
    options = ''.join([
              '-Wno-unused-result ',
              '-Wno-format-overflow ',
              '-Wno-return-local-addr ',
              '-Wno-stringop-overflow ',
              '-Wno-stringop-truncation ',
              '-Wno-maybe-uninitialized ',
              '-Wno-alloc-size-larger-than ',
              '-Wno-aggressive-loop-optimizations'])
    pisitools.cflags.add("%s" % options)

    mesontools.configure("-D use_libuv=true \
                          -D use_webui=true \
                          -D use_sys_lz4=true \
                          -D use_sys_zip=true \
                          -D use_sys_zlib=true \
                          -D use_sys_magic=true \
                          -D use_sys_xxhash=true \
                          -D use_sys_openssl=true \
                          -D use_sys_capstone=true \
                          -D use_sys_tree_sitter=true")


def build():
    mesontools.build()


def install():
    mesontools.install()
    #pisitools.dosym("/usr/bin/radare2", "/usr/bin/r2")
    pisitools.dosym("/usr/share/man/man1/radare2.1.gz",
                    "/usr/share/man/man1/r2.1.gz")
