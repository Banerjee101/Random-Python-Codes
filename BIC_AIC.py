from __future__ import division
import os
from astropy.io import ascii
import numpy as np
import matplotlib.pyplot as plt

pha_bins = 568

data = ascii.read("bb_cpl_stat.txt")
pgstat = data['col2']
dof = data['col3']


AIC = 2*(pha_bins - dof) + pgstat
BIC = pgstat + (pha_bins - dof)*np.log(pha_bins)

#print "The BIC is :"+str(BIC)+"\n"

ascii.write([np.round(AIC,1),np.round(BIC,1)], 'AIC_BIC_output.txt', names=['AIC', 'BIC'], overwrite=True)
