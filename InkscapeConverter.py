#!/usr/bin/python

import sys
import os

import subprocess

print("This script uses Inkscape to allow you to convert all svg/eps/pdf files in this folder from one type to another. ")

input_type = raw_input("What type of file are you converting FROM? (svg / pdf / eps) ")

if not (input_type == "svg" or input_type == "pdf" or input_type == "eps"):
	print("This is not a valid type. The only valid types are svg or eps or pdf.")
	sys.exit()

output_type = raw_input("What type of file are you converting TO? (eps / pdf / png) ")

if not (output_type == "eps" or output_type == "pdf" or output_type == "png"):
	print("This is not a valid type. The only valid types are png or eps or pdf.")
	sys.exit()

# dpi_res = input("What dpi resolution? (default is 100)")

for f in sorted(os.listdir(os.getcwd())):
	if(f.endswith("."+input_type)):
		print ("Converting " + f )
		print subprocess.check_output(['inkscape', f, "--export-"+output_type+"="+f[:-3]+output_type, "--export-dpi=100"])


