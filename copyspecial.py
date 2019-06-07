#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse
import sys
import commands

# This is to help coaches and graders identify student assignments
__author__ = "jupiter2018"


# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
    """Get all filepaths in directory"""
    files_list = os.listdir(dir)
    special_files_list = []
    #print(files_list)
    for file in files_list:
        searchfile = re.search('__\w+__',file)
        if(searchfile):
            #print(os.path.abspath(file))
            special_files_list.append(os.path.abspath(file))
    return special_files_list
def copy_to(paths, dir):
    """Copy files to directory"""
    if not os.path.exists(dir):
        os.makedirs(dir)
    for path in paths:
        shutil.copy(path,dir)

def zip_to(paths, zip_path):
    """Zip up all of the given files into a new zip file with the given name."""
    cmd = 'zip -j ' + zip_path + ' ' + ' '.join(paths)
    print "Command I'm going to do:" + cmd
    (status, output) = commands.getstatusoutput(cmd)
    # If command had a problem (status is non-zero),
    # print its output to stderr and exit.
    if status:
        print(output)
        sys.exit(1)


def main():
    """main function starts here """
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', help='name of directory to search')
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    #print(args)
    if args.dir == '.':
        #print os.getcwd()
        files_to_transfer = get_special_paths(os.getcwd())
        #print(files_to_transfer)
        if args.todir :
            target_dir = args.todir
            print target_dir
            copy_to(files_to_transfer,target_dir)
        if args.tozip:
            target_zip = args.tozip
            zip_to(files_to_transfer,target_zip)
        if len(sys.argv) == 2:
            print('\n'.join(files_to_transfer))
        


    
    # Call your functions


if __name__ == "__main__":
    main()
