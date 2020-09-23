#!/usr/bin/python

import os

# FIXME
# bash script cannot set environment variables

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # to set some environmental variables
    try:
        os.system("source /etc/profile.d/emscripten.sh")
    except:
        pass
    
def postRemove():
    # to unset environmental variables
    try:
        os.system("export EM_IGNORE_SANITY=''")
        if(os.environ['PATH'].find("/usr/lib/emscripten") != -1):
            ver = os.environ['PATH'].replace("/usr/lib/emscripten", "")
    except:
        pass 