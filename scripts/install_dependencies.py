#!/usr/bin/env python2
import os, sys, json, subprocess, getopt, argparse


parser = argparse.ArgumentParser(description='SO test.')
parser.add_argument('files', nargs='*')  # This is it!!
args = parser.parse_args()
file_arg = args.files[0]

try:
	with open(file_arg, 'r') as json_file:
		data = json.load(json_file)
except IOError, ioe:
	# print "I/O error({0}): {1}".format(ioe.errno, ioe.strerror)
	print ioe
except ValueError, ve:
	# print "I/O error({0}): {1}".format(e.errno, e.strerror)
	print ve
	# raise
else:
	for django_package in data['dependencies']:
		# This won't work on many systems: majority of folks will have 2 pips by now
		# One for python 2.7.x and one for python 3.x hence naming them pip2 and pip3 or simarly
		# on my Arch pip is actually linked to pip3 which causes all crazy stuff
		# hence requirements.txt is the way forward :)
		command = ['pip', 'install', django_package]

		p = subprocess.Popen(command, stdout=subprocess.PIPE)
		output, err = p.communicate()
		print "\Installing " + django_package + " ....\n\n", output, '\n **** COMPLETE!\n'