import os
import math
import scipy
import texttable as tt
import itertools as itt
import numpy as np
from astropy.io import ascii
from astropy.io import fits
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches	
from matplotlib import rcParams, cycler 
from scipy import stats
import matplotlib as mpl

#####################################################################################################################################################

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
lstyle = 'None'


#For reading the data from ASCII
mo1_ifl_pgstat, mo1_ifl_dof = np.loadtxt("bb_bandC_results_stat.txt", unpack=True, usecols=[1,2])
mo2_ifl_pgstat, mo2_ifl_dof = np.loadtxt("GRB160509AA_three_comp_stat.txt", unpack=True, usecols=[1,2])
mo3_ifl_pgstat, mo3_ifl_dof = np.loadtxt("GRB160509A_bkn2powC_stat.txt", unpack=True, usecols=[1,2])
mo4_ifl_pgstat, mo4_ifl_dof = np.loadtxt("result_band_stat.txt", unpack=True, usecols=[1,2])
mo5_ifl_pgstat, mo5_ifl_dof = np.loadtxt("results_bandC_stat.txt", unpack=True, usecols=[1,2])
mo6_ifl_pgstat, mo6_ifl_dof = np.loadtxt("results_stat_bb_band.txt", unpack=True, usecols=[1,2])

LC1_time, LC1_rate=np.loadtxt("LC_LLE20000100000.qdp", unpack=True, usecols=[0, 1])
LC2_time, LC2_rate=np.loadtxt("LC_n3_1s830.qdp", unpack=True, usecols=[0, 1])

#####################################################################################################################################################

#setting the input parameters
pha_bins = 476									#Set the PHA bins from data (generalize this)
range1=8.5									#set the reference time for the plot
x_lim_min=7.5									#set the x limit minimum
x_lim_max=28.0									#set the x limit maximum
y_lim_max=650									#set the y limit maximum
corr_lim=6.0									#Set the correlation limit here
mo1,mo2,mo3,mo4,mo5,mo6='BB + BandC', 'BB + CPL + CPL', 'Bkn2powC', 'Band', 'BandC', 'BB + Band' #Set the model names here, same as input order

#####################################################################################################################################################

#This is for creating BIC 
Nlog = np.log(pha_bins)
mo1_BIC = mo1_ifl_pgstat + (pha_bins-mo1_ifl_dof)*Nlog
mo2_BIC = mo2_ifl_pgstat + (pha_bins-mo2_ifl_dof)*Nlog
mo3_BIC = mo3_ifl_pgstat + (pha_bins-mo3_ifl_dof)*Nlog
mo4_BIC = mo4_ifl_pgstat + (pha_bins-mo4_ifl_dof)*Nlog
mo5_BIC = mo5_ifl_pgstat + (pha_bins-mo5_ifl_dof)*Nlog
mo6_BIC = mo6_ifl_pgstat + (pha_bins-mo6_ifl_dof)*Nlog

#####################################################################################################################################################

#Subplot section that makes the 
fig, (ay1, ay2) = plt.subplots(2, sharex=True, gridspec_kw = {'height_ratios':[2, 1]})
lengthlist=len(mo1_BIC)
#if all(len(lst) == lengthlist for lst in [mo2_BIC, mo3_BIC, mo4_BIC, mo5_BIC, mo6_BIC]):
mo1_BICT,mo2_BICT,mo3_BICT,mo4_BICT,mo5_BICT,mo6_BICT=mo1_BIC[mo1_BIC<y_lim_max],mo2_BIC[mo2_BIC<y_lim_max],mo3_BIC[mo3_BIC<y_lim_max],mo4_BIC[mo4_BIC<y_lim_max],mo5_BIC[mo5_BIC<y_lim_max],mo6_BIC[mo6_BIC<y_lim_max]

plt.xlim([x_lim_min,x_lim_max])
ay1.plot(np.arange(range1, range1+len(mo1_BICT)), mo1_BICT, "v-", lw = 1.0, markersize=7, label=mo1, color='b')
ay1.plot(np.arange(range1, range1+len(mo2_BICT)), mo2_BICT, "^-", lw = 1.0, markersize=7, label=mo2, color='g')
ay1.plot(np.arange(range1, range1+len(mo3_BICT)), mo3_BICT, "<-", lw = 1.0, markersize=7, label=mo3, color='r')
ay1.plot(np.arange(range1, range1+len(mo4_BICT)), mo4_BICT, ">-", lw = 1.0, markersize=7, label=mo4, color='c')
ay1.plot(np.arange(range1, range1+len(mo5_BICT)), mo5_BICT, "*-", lw = 1.0, markersize=7, label=mo5, color='m')
ay1.plot(np.arange(range1, range1+len(mo6_BICT)), mo6_BICT, "8-", lw = 1.0, markersize=7, label=mo6, color='y')
ay11=ay1.twinx()
ay11.axis('off')
ay11.plot(LC1_time, LC1_rate, lw=1.0, ls='steps-post', label='LC1', color='gray')
ay12=ay1.twinx()
ay12.axis('off')
ay12.plot(LC2_time, LC2_rate, lw=1.0, ls='steps-post', label='LC2', color ='purple')
ay1.legend(numpoints=1,prop={'size':10},loc="upper right")

#combining the arrays into a text file
col_stack = np.column_stack((mo1_BIC, mo2_BIC, mo3_BIC, mo4_BIC, mo5_BIC, mo6_BIC))
col_stackT = col_stack.transpose()
np.savetxt('BIC_Stack.txt', col_stackT, delimiter='  ')
steps = 0
table=tt.Texttable(max_width=0)
headings=['Time Stamps', 'Models with ascending order of BICs', 'Delta BIC 1', 'Delta BIC 2', 'Delta BIC 3', 'Delta BIC 4', 'Delta BIC 5', 'Strong corellation model']
table.header(headings)
for h in range(0,np.size(col_stackT,1)):
	list1 = np.loadtxt("BIC_Stack.txt", unpack=True, usecols=[h])
	list2 = np.array(['a','b','c','d', 'e', 'f'])
	list3 = np.array([mo1, mo2, mo3, mo4, mo5, mo6])
	tups = zip(list1, list2, list3); tups.sort(); zip(*tups)
	d1=abs(tups[0][0]-tups[1][0])
	d2=abs(tups[0][0]-tups[2][0])
	d3=abs(tups[0][0]-tups[3][0])
	d4=abs(tups[0][0]-tups[4][0])
	d5=abs(tups[0][0]-tups[5][0])
	time_stamps=range1+steps
	plt.xlim(xmin=x_lim_min,xmax=x_lim_max)
	ay2.set_ylim([0,50])
	ay2.plot(time_stamps,d1,"-8", lw = 1.0, markersize=5, markerfacecolor="None",markeredgecolor='red')
	ay2.plot(time_stamps,d2,"-s", lw = 1.0, markersize=5, markerfacecolor="None",markeredgecolor='red')
	ay2.plot(time_stamps,d3,"-p", lw = 1.0, markersize=5, markerfacecolor="None",markeredgecolor='red')
	ay2.plot(time_stamps,d4,"-P", lw = 1.0, markersize=5, markerfacecolor="None",markeredgecolor='red')
	ay2.plot(time_stamps,d5,"-*", lw = 1.0, markersize=5, markerfacecolor="None",markeredgecolor='red')
	d11,d22,d33,d44,d55=d1[d1<50],d2[d2<50],d3[d3<50],d4[d4<50],d5[d5<50]
	m1,m2,m3,m4,m5,m6=tups[0][1],tups[1][1],tups[2][1],tups[3][1],tups[4][1],tups[5][1]
	ay2.text(time_stamps,d1, m1+m2, fontsize = 10)
	ay2.text(time_stamps,d2, m1+m3, fontsize = 10)
	ay2.text(time_stamps,d3, m1+m4, fontsize = 10)
	ay2.text(time_stamps,d4, m1+m5, fontsize = 10)
	ay2.text(time_stamps,d5, m1+m6, fontsize = 10)
	b_patch = mpatches.Patch(color='b', label='a='+mo1)
	g_patch = mpatches.Patch(color='g', label='b='+mo2)
	r_patch = mpatches.Patch(color='r', label='c='+mo3)
	c_patch = mpatches.Patch(color='c', label='d='+mo4)
	m_patch = mpatches.Patch(color='m', label='e='+mo5)
	y_patch = mpatches.Patch(color='y', label='f='+mo6)
	ay2.legend(handles=[b_patch, g_patch, r_patch, c_patch, m_patch, y_patch], fontsize = 9)
	steps=steps+1
	
	#Section to sort the strongest correlation model
	m11,m22,m33,m44,m55,m66=tups[0][2],tups[1][2],tups[2][2],tups[3][2],tups[4][2],tups[5][2]
	model_conv=''
	if d1<=corr_lim:
		model_conv='('+m11+') / ('+m22+')'
		if d2<=corr_lim:
			model_conv='('+m11+') / ('+m22+') / ('+m33+')'
			if d3<=corr_lim:
				model_conv='('+m11+') / ('+m22+') / ('+m33+') / ('+m44+')'
				if d4<=corr_lim:	
					model_conv='('+m11+') / ('+m22+') / ('+m33+') / ('+m44+') / ('+m55+')'
					if d5<=corr_lim:
						model_conv='all models have strong correlation to each other'

	elif d1>=corr_lim:
		model_conv=m11+' is the best fit model'
	for row in zip(itt.repeat(time_stamps, np.size(col_stackT,1)), ['('+m11+') < ('+m22+') < ('+m33+') < ('+m44+') < ('+m55+') < ('+m66+')'], [d11], [d22], [d33], [d44], [d55], [model_conv]):
		table.add_row(row)
s = table.draw()
print s
#ascii.write(s, 'TestTable1.txt', format='latex')	

#####################################################################################################################################################	

#This is the plotting section
ay2.axhline(y=2, color='black', lw=0.7)
ay2.axhline(y=6, color='black', lw=0.7)
ay2.axhline(y=10, color='black', lw=0.7)
ay2.set_xlabel('time (s)')
ay1.set_ylabel('BIC')
ay2.set_ylabel('delta(BIC)')
plt.subplots_adjust(hspace=0.00)
#~ plt.xscale('log')
#plt.tight_layout()
plt.show()
