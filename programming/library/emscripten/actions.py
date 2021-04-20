#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import mesontools
from pisi.actionsapi import shelltools

def setup():
    # we dont pull the sources via git, we should by pass git command
    pisitools.dosed("tools/install.py", "add_revision_file\(target\)\n",
                                        "#add_revision_file(target)\n")
    # suppress compiler warnings
    options = ''.join([
              '"-Wno-cast-qual ',
              '-Wno-array-bounds ',
              '-Wno-uninitialized ',
              '-Wno-unused-function ',
              '-Wno-unused-variable ',
              '-Wno-pessimizing-move ',
              '-Wno-init-list-lifetime ',
              '-Wno-cast-function-type ',
              '-Wno-stringop-truncation ',
              '-Wno-nonportable-include-path"'])

    # Inspired from https://github.com/WebAssembly/waterfall/blob/db2ea5eeb11b74cce9b9459be0cc88807744b1b5/src/build.py#L868
    shelltools.cd("llvm-project-llvmorg-12.0.0/llvm")
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-Bbuild \
                          -GNinja \
                          -DCMAKE_CXX_FLAGS=%s \
                          -DCMAKE_SKIP_RPATH=ON \
                          -DLLVM_BUILD_RUNTIME=OFF \
                          -DLLVM_TOOL_LTO_BUILD=ON \
                          -DLLVM_INCLUDE_TESTS=OFF \
                          -DLLVM_ENABLE_LIBXML2=OFF \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DLLVM_INCLUDE_EXAMPLES=OFF \
                          -DCOMPILER_RT_BUILD_XRAY=OFF \
                          -DCOMPILER_RT_ENABLE_IOS=OFF \
                          -DCOMPILER_RT_INCLUDE_TESTS=OFF \
                          -DLLVM_INSTALL_TOOLCHAIN_ONLY=ON \
                          -DLLVM_ENABLE_PROJECTS='lld;clang' \
                          -DLLVM_TARGETS_TO_BUILD='X86;WebAssembly' \
                          -DCMAKE_INSTALL_PREFIX=/opt/emscripten-llvm \
                          -DCLANG_INCLUDE_TESTS=OFF" % options, sourceDir="..")
    
def build():
    shelltools.cd("llvm-project-llvmorg-12.0.0/llvm/build")
    mesontools.build()

def install():
    """
    Install LLVM stuff according to
    https://github.com/emscripten-core/emscripten/blob/master/docs/packaging.md
    and
    https://github.com/WebAssembly/waterfall/blob/d4a504ffee488a68d09b336897c00d404544601d/src/build.py#L91
    """
    shelltools.cd("llvm-project-llvmorg-12.0.0/llvm/build")
    mesontools.install()
    
    # let's clean up some unnecessary binaries:
    for bindel in ["ld.lld",
                   "clang-check",
                   "clang-cl",
                   "lld-link",
                   "llvm-lib",
                   "clang-cpp",
                   "clang-format",
                   "clang-rename",
                   "clang-refactor",
                   "clang-scan-deps",
                   "clang-extdef-mapping",
                   "clang-offload-bundler"]:
        pisitools.remove("/opt/emscripten-llvm/bin/%s" % bindel)

    pisitools.remove("/opt/emscripten-llvm/lib/libclang.so")
    pisitools.removeDir("/opt/emscripten-llvm/share")
    
    # copy needed stuff which doesn't come by default
    for binneed in ["llc",
                    "opt",
                    "llvm-as",
                    "llvm-mc",
                    "llvm-dis",
                    "FileCheck",
                    "llvm-link",
                    "llvm-readobj",
                    "llvm-dwarfdump"]:
        pisitools.insinto("/opt/emscripten-llvm/bin/", "build/bin/%s" % binneed)
    
    # now install emscripten
    shelltools.cd("../../..")
    autotools.rawInstall("DESTDIR=%s/usr/lib/emscripten" % get.installDIR())

    # make symlinks under /usr/bin 'cuz i got problems on setting PATH
    for em_bin in ["em++",
                   "emar",
                   "emcc",
                   "emrun",
                   "emsize",
                   "emmake",
                   "em++.py",
                   "emar.py",
                   "emcc.py",
                   "emcmake",
                   "emscons",
                   "em++.bat",
                   "emcc.bat",
                   "emranlib",
                   "emar.bat",
                   "emrun.py",
                   "em-config",
                   "embuilder",
                   "emlink.py",
                   "emmake.py",
                   "emrun.bat",
                   "emsize.py",
                   "emmake.bat",
                   "emscons.py",
                   "emsize.bat",
                   "emcmake.py",
                   "emcmake.bat",
                   "emconfigure",
                   "emranlib.py",
                   "emscons.bat",
                   "embuilder.py",
                   "emranlib.bat",
                   "em-config.py",
                   "em-config.bat",
                   "embuilder.bat",
                   "emscripten.py",
                   "emconfigure.py",
                   "emconfigure.bat",
                   "emscripten-version.txt",
                   "emscripten-revision.txt"]:
        pisitools.dosym("/usr/lib/emscripten/%s" % em_bin,
                        "/usr/bin/%s" % em_bin)

    # create docs and make symlink
    pisitools.dosym("/usr/lib/emscripten/docs",
                    "/usr/share/doc/%s/docs" % get.srcNAME())

    pisitools.dodoc("LICENSE*", "README*")
