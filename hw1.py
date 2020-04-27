#!/usr/bin/python

import sys

if len(sys.argv) != 0:
	for file in sys.argv[1:]:
		with open(file, mode='r') as files:
			for line in files:
				line = line.replace("\r","").replace("\n","")
				print line
