
from __future__ import division
from scipy import special
import numpy as np
import sympy as sp
from scipy.integrate import quad
import matplotlib.pyplot as plt
from astropy.io import ascii
import matplotlib.gridspec as gridspec
from astropy.io import fits
from pylab import *
import matplotlib as mpl


def Band_function_flux(x, K, a, b, Ep):
	Eb = (a-b)*Ep/(2+a)
	if x < Eb:
		B = x*K*((x/100)**a)*np.exp(-x*(2+a)/Ep)
	else:
		B = x*K*(((a-b)*Ep/(100*(2+a)))**(a-b))*np.exp(b-a)*(x/100)**b
	return B

def Band_nu_Fnu(x, K, a, b, Ep):
	Eb = (a-b)*Ep/(2+a)
	if x < Eb:
		B = (x**2)*K*((x/100)**a)*np.exp(-x*(2+a)/Ep)
	else:
		B = (x**2)*K*(((a-b)*Ep/(100*(2+a)))**(a-b))*np.exp(b-a)*(x/100)**b
	return B
	
	
def BandC_nu_Fnu(x, K, a, b, Ep,Ef):
	Eb = (a-b)*Ep/(2+a)
	if x < Eb:
		B = (x**2)*K*((x/100)**a)*np.exp(-x*(2+a)/Ep)*np.exp(-x/Ef)
	else:
		B = (x**2)*K*(((a-b)*Ep/(100*(2+a)))**(a-b))*np.exp(b-a)*((x/100)**b)*np.exp(-x/Ef)
	return B	
	
	
	
def po_flux(x,K,a):
	return x*K*x**(-a)


def po_nu_Fnu(x,K,a):
	return (x**2)*K*x**(-a)

def cutoffpl_flux(x,K,a,Hc):
	return x*K*(x**(-a))*np.exp(-x/Hc)

def cutoffpl_flux_pivot_flux(x,K1,Epi,a,Hc):
	return x*K1*((x/Epi)**a)*np.exp(-x/Hc)
	
def bb_flux(x, K, T): # T is in keV
	return x*K*x**2/(np.exp(x/T)-1)
	
def flux_band(E1, E2, z, a, b, Ep, K):
	E11 = E1/(1+z)
	E22 = E2/(1+z)
	Ec = Ep/(2+a)
	Ebreak = (a-b)*Ec
	F = quad(Band_function_flux, E11, E22, args=(K, a, b, Ep))[0]
	return Ep, Ebreak, F

def flux_po(E1, E2, z, K, a):
	E1 = E1/(1+z)
	E2 = E2/(1+z)
	return quad(po_flux, E1, E2, args=(K, a))[0]
	
def flux_cutoffpl(E1, E2, z, K,a,Hc):
	E1 = E1/(1+z)
	E2 = E2/(1+z)
	return quad(cutoffpl_flux, E1, E2, args=(K, a, Hc))[0]	
	
def flux_cutoffpl_pivot(E1, E2, z, K1, Epi, a,Hc):
	E1 = E1/(1+z)
	E2 = E2/(1+z)
	return quad(cutoffpl_flux_pivot_flux, E1, E2, args=(K1,Epi,a, Hc))[0]	
	
def integration_z(x):
	return (1/(sp.sqrt(0.27*(1+x)**3 + 0.73)))


pc = 3.086e18
H = 70 * 100000 / (1e6 * pc)
c = 3.0e10
print H


def Lumi(Flux,z):
	D_L = c*(1+z)/H
	Int = quad(integration_z,0,z)
	Dist = D_L*Int[0]
	l = 4*np.pi*(Dist**2)*Flux
	return l

def Eiso(Flux,z, dur):
	D_L = c*(1+z)/H
	Int = quad(integration_z,0,z)
	Dist = D_L*Int[0]
	l = 4*np.pi*(Dist**2)*Flux*dur/(1+z)
	return l





# GRB 160509A
# Read data



#LAT data
lc_file = fits.open('gll_ft1_tr_bn160509374_v00_filt_gtsrcprob.fit','readonly')
GBM_TRIGTIME = lc_file[0].header['TRIGTIME']
pridata1 = lc_file[1].data
time = pridata1.field(9)
Energy = pridata1.field(0)
srcprob = pridata1.field(150)
lc_file.close()

T_arg = np.argsort(time  - GBM_TRIGTIME)
T = time[T_arg]- GBM_TRIGTIME

Energy = Energy[T_arg]
SRC_PROB = np.array(srcprob[T_arg])

ascii.write([T, Energy, SRC_PROB], 'LC_E_srcprob.txt', names=['time', 'E', 'prob'], overwrite=True)
#~ E_s = [Energy>1000]
#~ Energy = Energy[E_s]
#~ T = T[E_s]
#~ print T
#~ print len(T)
#~ print len(Energy)

T_min = np.min(T)
#~ T_min = 10.0
T_max = np.max(T)
#~ print "minimum Time is", np.min(T)
#~ print "maximum Time is", np.max(T)

hist, bin_edges = np.histogram(T, bins =int((T_max-T_min)))


# GBM

Band00 = ascii.read("LC_n0_1s830.qdp", header_start = None , data_start = 1)
Band01= ascii.read("LC_n1_1s830.qdp", header_start = None , data_start = 1 )
Band02= ascii.read("LC_n3_1s830.qdp", header_start = None , data_start = 1)

Band10 = ascii.read("LC_n0_1s30300.qdp", header_start = None , data_start = 1)
Band11= ascii.read("LC_n1_1s30300.qdp", header_start = None , data_start = 1 )
Band12= ascii.read("LC_n3_1s30300.qdp", header_start = None , data_start = 1)

# LLE
Band6 = ascii.read("LC_LLE20000100000.qdp", header_start = None , data_start = 1)

# Coarse time bins

c_time_bins = np.array([-1.47, 8, 13, 15, 16, 18, 21, 27, 38, 63, 80, 303, 362])




#PlOTS

x_pos = 60
alpha_val =0.5
#Customize plots

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

gs = gridspec.GridSpec(2, 1, height_ratios=[1,1])


#B0_time = np.array(Band10['col1'])
#B0_rate = np.array(Band10['col2'])+np.array(Band11['col2'])+np.array(Band12['col2'])
#B0_Bblocks = ascii.read("n_30_300_bins_wrt_Trigertime.txt", header_start = None , data_start = 1)
#B0_Bayesian_blocks =np.array(B0_Bblocks['col1'])
#B0_Bayesian_rate =np.array( B0_Bblocks['col3'])
#ax0 = plt.subplot(gs[0])
#ax0.plot(B0_time, B0_rate, '.', ls='step', color='k',linestyle='steps-post',markersize=0, markerfacecolor='none', markeredgecolor='k',lw = 3.0, alpha=alpha_val)
#ax0.plot(B0_Bayesian_blocks, B0_Bayesian_rate ,  '.', lw = 2.0, color='red',linestyle='steps-post', markersize=2, markerfacecolor='none', markeredgecolor='red', ms=0)

#~ ax0.set_ylabel(r'Counts/s',fontsize=18)
#ax0.get_yaxis().set_label_coords(-0.05,0.5)
#ax0.annotate('NaI 0+1+3\n30 - 300 keV', (x_pos, 2100), size=14)#, (265, 0.08), size=14)





LLE_time = np.array(Band6['col1'])
LLE_rate = np.array(Band6['col2'])


ax1 = plt.subplot(gs[0])
ax1.plot(LLE_time, LLE_rate , '.', ls='step', color='k',linestyle='steps-post',markersize=0, markerfacecolor='none', markeredgecolor='k', lw = 3.0, alpha=alpha_val)	
ax1.set_xlim([-10,90])
plt.xlim([-10,90])
ax1.annotate('LAT-LLE\n20 - 100 MeV', (x_pos, 250),  size=14)
##~ ax1.plot(LLE_Bayesian_blocks, LLE_Bayesian_rate ,  '.', lw = 2.0, color='red',linestyle='steps-post', markersize=2, markerfacecolor='none', markeredgecolor='red', ms=0)
##~ ax1.annotate('LAT-LLE\n20 - 100 MeV', (x_pos, 250),  size=14)


probability = 0.9
# src prob gt 90 %
src_gte_prob90 = [( probability <= SRC_PROB)]
print src_gte_prob90
Energy_gte_prob90 = Energy[src_gte_prob90]
print Energy_gte_prob90
T_gte_prob90= T[src_gte_prob90]
print SRC_PROB[src_gte_prob90]
# src prob lt 90 %

src_lt_prob90 = [(SRC_PROB < probability)]
#~ print src_gt_prob90
Energy_lt_prob90 = Energy[src_lt_prob90]
print Energy_lt_prob90
T_lt_prob90= T[src_lt_prob90]

mkersize=6
ax2 = ax1.twinx()
#~ ax2.plot(T, Energy, 'o', ms=8, color="g", markerfacecolor='none', markeredgecolor='g')
##~ ax2.set_xlim([-10,90])
ax2.plot(T_gte_prob90, Energy_gte_prob90, 'o', ms=mkersize, color="g", markerfacecolor='g', markeredgecolor='g')
ax2.plot(T_lt_prob90, Energy_lt_prob90, 'o', ms=mkersize, color="g", markerfacecolor='none', markeredgecolor='g')
ax2.set_xlabel(r'Time($s$)',fontsize=18)
ax2.set_ylabel(r'Energy($MeV$)',fontsize=18, color='g')
ax2.set_yscale('log')
ax2.tick_params('y', colors='g')
ax2.spines['right'].set_color('g')

B1_time = np.array(Band10['col1'])
B1_rate = np.array(Band00['col2'])+np.array(Band01['col2'])+np.array(Band02['col2'] + Band10['col2'])+np.array(Band11['col2'])+np.array(Band12['col2'])
##~ B1_Bblocks = ascii.read("n_30_300_bins_wrt_Trigertime.txt", header_start = None , data_start = 1)
##~ B1_Bayesian_blocks =np.array( B1_Bblocks['col1'])
##~ B1_Bayesian_rate =np.array( B1_Bblocks['col3'])
ax3 = plt.subplot(gs[1], sharex = ax1)
ax3.plot(B1_time,B1_rate, '.', ls='step', color='k',linestyle='steps-post',markersize=0, markerfacecolor='none', markeredgecolor='k',lw = 3.0, alpha=alpha_val)
##~ ax8.plot(B1_Bayesian_blocks, B1_Bayesian_rate ,  '.', lw = 2.0, color='red',linestyle='steps-post', markersize=2, markerfacecolor='none', markeredgecolor='red', ms=0)
#~ ax3.set_ylabel(r'Counts/s',fontsize=18)
ax3.get_yaxis().set_label_coords(-0.05,0.5)
ax3.annotate('NaI 0+1+3\n8 - 300 keV', (x_pos, 9800), size=14)#, (265, 0.08), size=14)


ax1.axvline(x=c_time_bins[1], ymin=0.0, linewidth=1.0, color='k',lw = 1.3, ls=':')
ax1.axvline(x=c_time_bins[2], ymin=0.0, linewidth=1.0, color='k',lw = 1.3, ls=':')
ax1.axvline(x=c_time_bins[3], ymin=0.0, linewidth=1.0, color='k',lw = 1.3, ls=':')
ax1.axvline(x=c_time_bins[4], ymin=0.0, linewidth=1.0, color='k',lw = 1.3, ls=':')
ax1.axvline(x=c_time_bins[5], ymin=0.0, linewidth=1.0, color='k',lw = 1.3, ls=':')
ax1.axvline(x=c_time_bins[6], ymin=0.0, linewidth=1.0, color='k',lw = 1.3, ls=':')
ax1.axvline(x=c_time_bins[7], ymin=0.0, linewidth=1.0, color='k',lw = 1.3, ls=':')
ax1.axvline(x=c_time_bins[8], ymin=0.0, linewidth=1.0, color='k',lw = 1.3, ls=':')
ax3.axvline(x=c_time_bins[1], ymin=0.0, linewidth=1.0, color='k',lw = 1.3, ls=':')
ax3.axvline(x=c_time_bins[2], ymin=0.0, linewidth=1.0, color='k',lw = 1.3, ls=':')
ax3.axvline(x=c_time_bins[3], ymin=0.0, linewidth=1.0, color='k',lw = 1.3, ls=':')
ax3.axvline(x=c_time_bins[4], ymin=0.0, linewidth=1.0, color='k',lw = 1.3, ls=':')
ax3.axvline(x=c_time_bins[5], ymin=0.0, linewidth=1.0, color='k',lw = 1.3, ls=':')
ax3.axvline(x=c_time_bins[6], ymin=0.0, linewidth=1.0, color='k',lw = 1.3, ls=':')
ax3.axvline(x=c_time_bins[7], ymin=0.0, linewidth=1.0, color='k',lw = 1.3, ls=':')
ax3.axvline(x=c_time_bins[8], ymin=0.0, linewidth=1.0, color='k',lw = 1.3, ls=':')





plt.legend(prop={'size':11}, loc = 'best')

xticklabels =ax1.get_xticklabels()
#~ yticklabels = ax3.get_yticklabels() 
#~ plt.setp(yticklabels, visible=False)
plt.setp(xticklabels, visible=False)
plt.subplots_adjust(hspace=0.0)
fig.text(0.02, 0.5, 'Counts/sec', rotation="vertical", va="center", fontsize=18)
plt.xlabel(r'Time since GBM trigger$\/$(s)',fontsize=18)

plt.show()















