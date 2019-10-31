
from __future__ import division
import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt

alpha = ascii.read("LAT_HE_cross_cor_10_40.qdp", header_start = None, data_start=0)


a = np.array(alpha['col1'])
b = np.array(alpha['col2'])
c = np.sqrt(b)


ascii.write([np.round(a,5), np.round(b,5), np.round(c,5)], "lat_crosscorr.txt", names=[ 'T1','rate', 'err'])
