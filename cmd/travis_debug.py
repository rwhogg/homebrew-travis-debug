#!/usr/bin/env python2

#
# Description: Test a Homebrew formula in the Travis CI environment 
# Author: Bob W. Hogg
# Usage: FIXME FIXME FIXME
#

from distutils.spawn import find_executable;
import os;
import subprocess;
import sys;

developer = "rwhogg";
repo_name = "homebrew-travis-debug";
repo_full_name = developer + "/" + repo_name;

# Find this directory
this_dir = subprocess.check_output(["brew", "--repo", repo_full_name]).strip("\n");
os.chdir(this_dir);

# check to make sure docker is available
docker = find_executable("docker");
if not docker:
    print "Error: please run \"brew install docker\""
    sys.exit(1);

# build the Docker image
# FIXME: need to be smarter about not rebuilding excessively
my_image_tag = repo_full_name;
subprocess.call([docker, "build", "--tag=" + my_image_tag, "."]);

# FIXME: the command is WRONG
subprocess.call([docker, "run", "-it", my_image_tag, "/bin/bash"]);
