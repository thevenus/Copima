# -*- coding: utf-8 -*-
"""
Author: Fuad Zadeh
Description: A small python program coping files from one folder to another folder
Program: Copima
"""
import glob, os
from shutil import copy2

def file_name(f):
    file_name = f.split('/')
    return file_name[-1]

# src for source folder which contains files
# dst for destination folder which files will copied
# filex for file extension

#-----Getting source directory---------------------------------------------------------------------------------
src = raw_input("Type in your source folder's directory\n> ")
while (not os.path.exists(src)):
    print "[ ERROR ] source directory not found"
    src = raw_input("Retype in your source folder's directory\n> ")

#-----Getting destination directory----------------------------------------------------------------------------
dst = raw_input("Type in your destination folder's directory\n> ")
if (not os.path.exists(dst)):
    print "[ ERROR ] destination directory not found"

    new_folder = raw_input("Want you make new folder in this name?\n[y/n]> ")
    if new_folder=='y'or new_folder=='Y':
        os.makedirs(dst)
        print "%s directory created"%dst
    else:
        print "Copima is exiting..."
        exit(0)

#-------Getting files extension--------------------------------------------------------------------------------
filex = raw_input("Type in your file extension(without dot in the beginning) that you want to copy from '%s'\n> " %src)

for file in glob.glob('%s*%s'%(src,filex)):
    copy2(file, dst)
    print " '%s' " %file_name(file)




