#!/usr/bin/python

import sys
import os

if len(sys.argv) != 3:
	print("usage: rename_file_subs.py OLD_SUBSTRING NEW_SUBSTRING")
else:
	print("This script will rename the following files:")
	file2rename = list()
	i = 0
	for f in sorted(os.listdir(os.getcwd())):
		if f.find(sys.argv[1]) != -1:
			file2rename.append(f)
			print file2rename[i]
			i += 1

	print("***")
	print("Into:")
	print("***")

	for f in file2rename:
		print f.replace(sys.argv[1],sys.argv[2])

	confirm = raw_input("Are you sure? (y/n) ")

	if confirm == "y":
		for f in file2rename:
			os.rename(f, f.replace(sys.argv[1],sys.argv[2]))