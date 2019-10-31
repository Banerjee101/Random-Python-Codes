from __future__ import division
import os
from astropy.io import ascii
import numpy as np
import matplotlib  
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec



bgo_band = ascii.read("LC_b1_1s_300-1000.qdp", header_start = None, comment = '#', data_start = 1)
nai_band = ascii.read("LC_n6_1s_8-900.qdp", header_start = None, comment = '#', data_start = 1)
soft_band = ascii.read("LC_n6_1s_8-30.qdp", header_start = None, comment = '#', data_start = 1)
hard_band = ascii.read("LC_n6_1s_50-300.qdp", header_start = None, comment = '#', data_start = 1)

print "Reading data for Soft Band 8 - 50 keV \n"
print soft_band
print "\n"

print "Reading data for Hard Band 50 - 300 keV \n"
print hard_band 
print "\n"

x1 = np.array(soft_band['col1'])
y1 = np.array(soft_band['col2'])
sy1 = np.array(soft_band['col3'])


x2 = np.array(hard_band['col1'])
y2 = np.array(hard_band['col2'])
sy2 = np.array(hard_band['col3'])

x1_bgo = np.array(bgo_band['col1'])
y1_bgo = np.array(bgo_band['col2'])
sy1_bgo = np.array(bgo_band['col3'])

x1_nai = np.array(nai_band['col1'])
y1_nai = np.array(nai_band['col2'])
sy1_nai = np.array(nai_band['col3'])


fig, axs = plt.subplots(4, sharex=True)

spectral_ratio = (y2)/(y1)
spectral_ratio_err = np.sqrt((y2**2)*sy1**2 +  (y1**2)*sy2**2)/y1**2

axs[0].errorbar(x1_bgo, y1_bgo, yerr=sy1_bgo, fmt = '.', capsize=0, markerfacecolor='k',color='k', ms=0, markeredgewidth=0, markeredgecolor='k', ls='steps-mid')
axs[1].errorbar(x1_nai, y1_nai, yerr=sy1_nai, fmt = '.', capsize=0, markerfacecolor='k',color='k', ms=0, markeredgewidth=0, markeredgecolor='k', ls='steps-mid')
axs[2].errorbar(x1, y1, yerr=sy1, fmt = '.', capsize=0, markerfacecolor='lawngreen',color='lawngreen', ms=0, markeredgewidth=0, markeredgecolor='lawngreen', ls='steps-mid')
axs[2].errorbar(x2, y2, yerr=sy2, fmt = '.', capsize=0, markerfacecolor='darkturquoise',color='darkturquoise', ms=0, markeredgewidth=0, markeredgecolor='darkturquoise', ls='steps-mid')
axs[3].errorbar(x1, spectral_ratio, yerr=spectral_ratio_err, fmt = '.', capsize=0, markerfacecolor='darkgray',color='darkgray', ms=0, markeredgewidth=0, markeredgecolor='darkgray', ls='steps-mid')
# ~ axs[2].errorbar(x1, spectral_ratio, fmt = '.', capsize=0, markerfacecolor='b',color='b', ms=0, markeredgewidth=0, markeredgecolor='k', ls='steps-mid')
#plt.xscale('log')
#plt.yscale('log')
#plt.show()

#print len(pulse1_rise['col1'])
#print len(pulse1_fall['col1'])



#plt.xscale('log')
# ~ plt.yscale('log')
axs[0].set_ylim(0.1,3000)
axs[1].set_ylim(0.1,2980)
axs[2].set_ylim(0,2499)
# ~ axs[0].set_ylim(0,2500)
# ~ axs[0].set_ylabel('counts s$^{-1}$')
axs[1].set_ylabel('counts s$^{-1}$')
# ~ axs[2].set_ylabel('counts s$^{-1}$')
# ~ axs[0].set_ylabel('counts s$^{-1}$')
plt.ylabel(r'Hard / Soft',fontsize= 9 )
plt.subplots_adjust(hspace=0)

# ~ xticklabels =axs[0].get_xticklabels() 
# ~ yticklabels = axs[0].get_yticklabels()
# ~ plt.setp(yticklabels, visible=False)
# ~ plt.setp(xticklabels, visible=False)



plt.xlim(-10,80)
plt.ylim(-3, 7)
plt.axhline(y=1.0, xmin=0.0, linewidth=2.0, color='mediumslateblue',ls='-')

axs[0].axvline(x=0.512, linewidth=1.0, color='fuchsia',ls='--')
axs[0].axvline(x=1.536, linewidth=1.0, color='fuchsia',ls='--')
axs[0].axvline(x=51.200, linewidth=1.0, color='fuchsia',ls='--')
axs[0].axvline(x=52.224, linewidth=1.0, color='fuchsia',ls='--')

axs[0].axvline(x=-0.640, linewidth=1.0, color='blue',ls='--')
axs[0].axvline(x=8.063, linewidth=1.0, color='blue',ls='--')
axs[0].axvline(x=47.04, linewidth=1.0, color='blue',ls='--')
axs[0].axvline(x=62.464, linewidth=1.0, color='blue',ls='--')

axs[1].axvline(x=0.512, linewidth=1.0, color='fuchsia',ls='--')
axs[1].axvline(x=1.536, linewidth=1.0, color='fuchsia',ls='--')
axs[1].axvline(x=51.200, linewidth=1.0, color='fuchsia',ls='--')
axs[1].axvline(x=52.224, linewidth=1.0, color='fuchsia',ls='--')
	
axs[1].axvline(x=-0.640, linewidth=1.0, color='blue',ls='--')
axs[1].axvline(x=8.063, linewidth=1.0, color='blue',ls='--')
axs[1].axvline(x=47.04, linewidth=1.0, color='blue',ls='--')
axs[1].axvline(x=62.464, linewidth=1.0, color='blue',ls='--')

axs[2].axvline(x=0.512, linewidth=1.0, color='fuchsia',ls='--')
axs[2].axvline(x=1.536, linewidth=1.0, color='fuchsia',ls='--')
axs[2].axvline(x=51.200, linewidth=1.0, color='fuchsia',ls='--')
axs[2].axvline(x=52.224, linewidth=1.0, color='fuchsia',ls='--')

axs[2].axvline(x=-0.640, linewidth=1.0, color='blue',ls='--')
axs[2].axvline(x=8.063, linewidth=1.0, color='blue',ls='--')
axs[2].axvline(x=47.04, linewidth=1.0, color='blue',ls='--')
axs[2].axvline(x=62.464, linewidth=1.0, color='blue',ls='--')

axs[3].axvline(x=0.512, linewidth=1.0, color='fuchsia',ls='--')
axs[3].axvline(x=1.536, linewidth=1.0, color='fuchsia',ls='--')
axs[3].axvline(x=51.200, linewidth=1.0, color='fuchsia',ls='--')
axs[3].axvline(x=52.224, linewidth=1.0, color='fuchsia',ls='--')

axs[3].axvline(x=-0.640, linewidth=1.0, color='blue',ls='--')
axs[3].axvline(x=8.063, linewidth=1.0, color='blue',ls='--')
axs[3].axvline(x=47.04, linewidth=1.0, color='blue',ls='--')
axs[3].axvline(x=62.464, linewidth=1.0, color='blue',ls='--')

mask_1 = (x1_nai >= -0.640) & (x1_nai <= 8.603)
mask_2 = (x1_nai >= 47.04) & (x1_nai <= 62.464)
for mr1 in range(len(mask_1)):
	if (mask_1[mr1] == True):
		axs[0].bar(x1_bgo[mr1],y1_bgo[mr1], color='khaki',width=1)
		axs[1].bar(x1_nai[mr1],y1_nai[mr1], color='khaki',width=1)
		# ~ axs[2].bar(x1[mr1],y1[mr1], color='khaki',width=1)
for mr2 in range(len(mask_2)):
	if (mask_2[mr2] == True):
		axs[0].bar(x1_bgo[mr2],y1_bgo[mr2], color='khaki',width=1)
		axs[1].bar(x1_nai[mr2],y1_nai[mr2], color='khaki',width=1)
		# ~ axs[2].bar(x1[mr2],y1[mr2], color='khaki',width=1)
# ~ print mask_1
# ~ axs[0].axvspan(xmin=-0.640, xmax=8.063, ymax=1000)
# ~ axs[1]
# ~ axs[2]

# ~ -0.640
# ~ 8.063
# ~ 47.04,
# ~ 62.464


Vert_lines = ascii.read("vert_line_plot_coord.txt", header_start = None, data_start = 0)


# ~ for vert in list(Vert_lines):
	# ~ print (vert)
	# ~ axs[0].axvline(x=vert, linestyle=':', color='darkgreen')
	# ~ axs[1].axvline(x=vert, linestyle=':', color='darkgreen')
	# ~ axs[2].axvline(x=vert, linestyle=':', color='darkgreen')
	# ~ axs[3].axvline(x=vert, linestyle=':', color='darkgreen')



plt.axhline(y=0.0, xmin=0.0, linewidth=2.0, color='k',ls='-')
axs[3].set_xlabel(r'Time since GBM trigger$\/$(s)',fontsize=9)
plt.show()












