from __future__ import division
import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from astropy.io import fits
from pylab import *
import matplotlib as mpl

detector = ['n4','BG']
emax, emin = 50, 300
bgE1, bgE2, bgE3 = 400, 1000, 40000

# Read data
Band00 = ascii.read("LC_"+detector[0]+"_fr_"+str(emax)+"_"+str(emin)+".qdp", header_start = None , data_start = 1)

Band1 = ascii.read("LC_"+detector[1]+"_"+str(bgE1)+"_"+str(bgE2)+".qdp", header_start = None , data_start = 1)
Band2 = ascii.read("LC_"+detector[1]+"_"+str(bgE2)+"_"+str(bgE3)+".qdp", header_start = None , data_start = 1)

Vert_lines = ascii.read("50SNR_Tbins.txt", header_start = None, data_start = 1)

Band0_rate = np.array(Band00['col2'])




x_pos = 8
alpha_val =0.5

font = {
        'weight' : 'bold',
        'size'   : 15}

mpl.rc('font', **font)
mpl.rcParams['axes.linewidth'] = 2
mpl.rcParams['axes.labelweight']='bold'
mpl.rcParams['axes.labelsize']='large'
mpl.rcParams['xtick.major.size'] = 4
mpl.rcParams['xtick.major.width'] = 2
mpl.rcParams['ytick.major.size'] = 4
mpl.rcParams['ytick.major.width'] = 2

l=3
das = (2, 8)
lw_dot = 3
fig = plt.figure(figsize=(10,6))
gs = gridspec.GridSpec(3, 1)



B2_time = np.array(Band2['col1'])
B2_rate = np.array(Band2['col2'])
ax1 = plt.subplot(gs[0])
ax1.plot(B2_time,B2_rate, '.', ls='step', color='k',linestyle='steps-post',markersize=0, markerfacecolor='none', markeredgecolor='k',lw = 3.0, alpha=alpha_val)
ax1.annotate('BGO 0 \n 1-40 MeV', (x_pos, 4000), size=14)
ax1.set_ylim([0,5900])

B1_time = np.array(Band1['col1'])
B1_rate = np.array(Band1['col2'])
ax2 = plt.subplot(gs[1], sharex = ax1)
ax2.plot(B1_time,B1_rate, '.', ls='step', color='k',linestyle='steps-post',markersize=0, markerfacecolor='none', markeredgecolor='k',lw = 3.0, alpha=alpha_val)
ax2.annotate('BGO 0 \n .4-1 MeV', (x_pos, 7000), size=14)

B0_time = np.array(Band00['col1'])
B0_rate = np.array(Band00['col2'])
ax3 = plt.subplot(gs[2], sharex = ax1)
ax3.plot(B0_time,B0_rate, '.', ls='step', color='k',linestyle='steps-post',markersize=0, markerfacecolor='none', markeredgecolor='k',lw = 3.0, alpha=alpha_val)
ax3.annotate('NaI n4 \n 50-300 KeV', (x_pos, 13000), size=14)
ax3.set_ylim([0,19899])



for vert in list(Vert_lines):
	# ~ print (vert)
	ax1.axvline(x=vert, linestyle=':')
	ax2.axvline(x=vert, linestyle=':')
	ax3.axvline(x=vert, linestyle=':')


plt.xlim([-1,10])
plt.xlabel(r'Time since GBM trigger$\/$(s)',fontsize=18)
xticklabels = ax2.get_xticklabels() + ax1.get_xticklabels()
yticklabels = ax3.get_yticklabels() + ax2.get_yticklabels()
# ~ plt.setp(yticklabels, visible=False)
plt.setp(xticklabels, visible=False)
plt.subplots_adjust(hspace=0.00)
fig.text(0.03, 0.5, '$Counts \ s^{-1}$', rotation="vertical", va="center", fontsize=18)
plt.show()




