#!/usr/bin/python
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
		command = ['pip', 'install', django_package]

		p = subprocess.Popen(command, stdout=subprocess.PIPE)
		output, err = p.communicate()
		print "\Installing " + django_package + " ....\n\n", output, '\n **** COMPLETE!\n'