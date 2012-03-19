#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys, getopt
from laminatebow import LaminateBow

def Usage():
	"""Show usage information"""
	print
	print "Usage: laminatelength [OPTIONS]"
	print
	print "OPTIONS:"
	print	
	print " -l, --length="
	print "  length of longest laminate"
	print
	print " -a, --layers="
	print "  number of layers"
	print
        print " -h, --help"
	print "  view this help message"
	print

def main():
	"""The main program"""

	# Some default variables
	maxlength = None
	layers = None
	
	# Parse the command line argument(s)
	try:
		# Arguments that are followed by a : require a value
		opts, args = getopt.getopt(sys.argv[1:], "hl:a:", ["help", "length=", "layers="])
	except getopt.GetoptError:
		Usage()
		sys.exit(1)
			
	for o, a in opts:
		if o in ("-h","--help"):
			Usage()
		if o in ("-l", "--length"):
			maxlength = a	
		if o in ("-a", "--layers"):
			layers = a

	if maxlength == None or layers == None:
		Usage()
		exit(1)

        laminatebow = LaminateBow(float(maxlength), int(layers))
        print laminatebow

if __name__ == "__main__":
	main()
