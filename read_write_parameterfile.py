#!/usr/bin/python

# Open a file
 
for i in range(1, 25):
	fo = open("GRB190114Cinfo_fitpar_individual_bb_band_pgstat"+str(i), "rw+")
	#~ print "Name of the file: ", fo.name
	line = fo.readline()
	print line
	line_string = line
