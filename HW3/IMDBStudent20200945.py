#!/usr/bin/python3

import sys

rslt = dict()

with open(sys.argv[1], "rt") as f:
	for line in f:
		array = line.split("::")
		rsltArray = array[2].split("|")
		for i in rsltArray:
			if i.strip() not in rslt:
				rslt[i.strip()] = 1
			else:
				rslt[i.strip()] += 1

with open(sys.argv[2], "wt") as f:
	for key in rslt.keys():
		f.write(key)
		f.write(" ")
		f.write(str(rslt[key]))
		f.write("\n")
