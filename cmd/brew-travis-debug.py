#!/usr/bin/env python2

#
# Description: Test a Homebrew formula in the Travis CI environment 
# Author: Bob W. Hogg
# Usage: FIXME FIXME FIXME
#

from distutils.spawn import find_executable;
import subprocess;
import sys;

docker = find_executable("docker");
if not docker:
    print "Error: please run \"brew install docker\""
    sys.exit(1);

my_image_tag = "rwhogg/homebrew-travis-debug";
subprocess.call([docker, "build", ".", "-t", my_image_tag]);

# FIXME: the command is WRONG
subprocess.call([docker, "run", "-it", my_image_tag, "/bin/bash"]);
