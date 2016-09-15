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

def error(msg):
    print "Error: " + msg; 
    sys.exit(1);

developer = "rwhogg";
repo_name = "homebrew-travis-debug";
repo_full_name = developer + "/" + repo_name;

# Find this directory
this_dir = subprocess.check_output(["brew", "--repo", repo_full_name]).strip("\n");
os.chdir(this_dir);

# check to make sure docker is available
docker = find_executable("docker");
if not docker:
    error("please run \"brew install docker\"");

# build the Docker image
# FIXME: need to be smarter about not rebuilding excessively
my_image_tag = repo_full_name;
result = subprocess.call([docker, "build", "--tag=" + my_image_tag, "."]);
if result != 0:
    print "Error: Docker image did not build correctly.";
    sys.exit(result);

# FIXME: the command is WRONG
subprocess.call([docker, "run", "-it", my_image_tag, "/bin/bash"]);
