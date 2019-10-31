from __future__ import division

from astropy.io import ascii
import os
import numpy as np



ifl = ascii.read("bb_and_4s_pars.txt", header_start = None, comment = '#')

print ifl



create_file = "echo \"\" > table10.txt"
os.system(create_file)
ofile = open("table10.txt", 'r+')
tab = []
for i in range(0,len(ifl['col1'])):
	 tab.append([str(round(ifl['col'+str(3*j+1)][i] , 3) )+'_{'+str(round(ifl['col'+str(3*j+2)][i], 3))+'}^{'+str(round(ifl['col'+str(3*j+3)][i], 3))+'}' for j in range(1,8)])
	 
for i in range(len(tab)):
	ofile.write(str(tab[i])+'\n')
ofile.close()
