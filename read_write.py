
from __future__ import division
import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt


GRB_name = 'GRB160509A'


#Bayesian blocks input in GRB160509A_n3_Bblocks
alpha = ascii.read(GRB_name+"_n3_Bblocks", header_start = None, data_start=0)

a = np.array(alpha['col1'])
b = np.array(alpha['col2'])
c = b-a


# ~ TRIGTIME = 484477130.219
# ~ background =163.382044314624011

# ~ a1 = a-TRIGTIME
# ~ b1 = b-TRIGTIME
c1 = np.array(alpha['col3'])#-background
d1 = np.array(alpha['col3'])


ascii.write([np.round(a1,3), np.round(b1,3), d1, np.round(c,3), np.round(c1,3)], GRB_name+"_n3_wrt_Trigertime.txt", names=[ 'T1','T2','rate', 'dur','net_counts'])
