from __future__ import division
import os
from astropy.io import ascii
import numpy as np
import matplotlib  
matplotlib.use('TkAgg')  
import matplotlib.pyplot as plt


# Read LC files from an ascii file listed as table
lc_files = ascii.read("b1_ascii_1024ms.dat", header_start = None, data_start=140)
print lc_files

E_channels = ascii.read("b1_ascii_1024ms.dat", header_start = None, data_start=11, data_end = 138 )
print E_channels

# ~ print lc_files['col1'][0]
# ~ print lc_files['col1'][1]
# ~ print lc_files['col1'][2]
# ~ print lc_files['col1'][3]
# ~ print lc_files['col3'][0]
# ~ print lc_files['col3'][1]


#Extracting the light curve



def LC(E_start, E_stop,t_start, t_stop):
	for i in range(len(lc_files)):
	    if ( lc_files['col1'][i] <= t_start ) and ( lc_files['col1'][i+1] > t_start ):
		    t_start_n = i
	for i in range(len(lc_files)):
	    if ( lc_files['col1'][i] <= t_stop ) and ( lc_files['col1'][i+1] > t_stop ):
		    t_stop_n = i
	print "Start time is: ", t_start_n
	print "Stop time is: ", t_stop_n
	for i in range(len(E_channels)):
		if ( E_channels['col1'][i] <= E_start ) and ( E_channels['col1'][i+1] > E_start ):
			E_start_n = i
	for i in range(len(E_channels)):
		if ( E_channels['col1'][i] <= E_stop ) and ( E_channels['col1'][i+1] > E_stop ):
			E_stop_n = i
	print "Start Energy is: ", E_channels['col1'][E_start_n]
	print "Stop Energy is: ", E_channels['col1'][E_stop_n]
	counts = []
	counts_error = []
	for i in range(t_start_n,t_stop_n+1):
		count = 0.0
		err_count = 0.0
		for k in range(E_start_n,E_stop_n):
			p = 4*k+3
			e_p = 4*k+4
			q = 4*k+5
			e_q = 4*k+6
			count =  count + lc_files['col'+str(p)][i] - lc_files['col'+str(q)][i]
			x1 = lc_files['col'+str(e_p)][i]
			x2 = lc_files['col'+str(e_q)][i]
			err_count=err_count+ (x1)**2+(x2)**2
		print lc_files['col1'][i], count, np.sqrt(err_count)
		counts.append(count)
		counts_error.append(np.sqrt(err_count))
	counts_array = np.array(counts)
	counts_error_array = np.array(counts_error)
	counts_plt_t = lc_files['col1'][t_start_n:t_stop_n+1]
	label_pl = str(E_start)+" - "+str(E_stop)+ " keV GBM/n3"
	return (counts_plt_t,counts_array,counts_error_array,label_pl)



# BGO

# Read LC files from an ascii file listed as table
# ~ lc_files_BG = ascii.read("b1_fr_ascii.dat", header_start = None, data_start=140)
# ~ print lc_files_BG

# ~ E_channels_BG = ascii.read("b1_fr_ascii.dat", header_start = None, data_start=11, data_end = 138 )
# ~ print E_channels_BG

# ~ print lc_files_BG['col1'][0]
# ~ print lc_files_BG['col1'][1]
# ~ print lc_files_BG['col1'][2]
# ~ print lc_files_BG['col1'][3]
# ~ print lc_files_BG['col3'][0]
# ~ print lc_files_BG['col3'][1]


#Extracting the light curve



def LCBGO(E_start, E_stop,t_start, t_stop):
	for i in range(len(lc_files_BG)):
	    if ( lc_files_BG['col1'][i] <= t_start ) and ( lc_files_BG['col1'][i+1] > t_start ):
		    t_start_n = i
	for i in range(len(lc_files_BG)):
	    if ( lc_files_BG['col1'][i] <= t_stop ) and ( lc_files_BG['col1'][i+1] > t_stop ):
		    t_stop_n = i
	print "Start time is: ", t_start_n
	print "Stop time is: ", t_stop_n
	for i in range(len(E_channels_BG)):
		if ( E_channels_BG['col1'][i] <= E_start ) and ( E_channels_BG['col1'][i+1] > E_start ):
			E_start_n = i
	for i in range(len(E_channels_BG)):
		if ( E_channels_BG['col1'][i] <= E_stop ) and ( E_channels_BG['col1'][i+1] > E_stop ):
			E_stop_n = i
	print "Start Energy is: ", E_channels_BG['col1'][E_start_n]
	print "Stop Energy is: ", E_channels_BG['col1'][E_stop_n]
	counts = []
	counts_error = []
	for i in range(t_start_n,t_stop_n+1):
		count = 0.0
		err_count = 0.0
		for k in range(E_start_n,E_stop_n):
			p = 4*k+3
			e_p = 4*k+4
			q = 4*k+5
			e_q = 4*k+6
			count = count + lc_files_BG['col'+str(p)][i]# -lc_files_BG['col'+str(q)][i]
			x1 = lc_files_BG['col'+str(e_p)][i]
			x2 = lc_files_BG['col'+str(e_q)][i]
			err_count=err_count+(x1)**2#+(x2)**2
		print lc_files_BG['col1'][i], count, np.sqrt(err_count)
		counts.append(count)
		counts_error.append(np.sqrt(err_count))
	counts_array = np.array(counts)
	counts_error_array = np.array(counts_error)
	counts_plt_t = lc_files_BG['col1'][t_start_n:t_stop_n+1]
	label_pl = str(E_start)+" - "+str(E_stop)+ " keV GBM/b0"
	return (counts_plt_t,counts_array,counts_error_array,label_pl)


# LLE

# Read LC files from an ascii file listed as table
# ~ lc_files_LLE = ascii.read("gll.dat", header_start = None, data_start=62)
# ~ print lc_files_LLE
  
# ~ E_channels_LLE = ascii.read("gll.dat", header_start = None, data_start=11, data_end = 60 )
# ~ print E_channels_LLE
  
# ~ print lc_files_LLE['col1'][0]
# ~ print lc_files_LLE['col1'][1]
# ~ print lc_files_LLE['col1'][2]
# ~ print lc_files_LLE['col1'][3]
# ~ print lc_files_LLE['col3'][0]
# ~ print lc_files_LLE['col3'][1]



def LCLLE(E_start, E_stop,t_start, t_stop):
	for i in range(len(lc_files_LLE)):
	    if ( lc_files_LLE['col1'][i] <= t_start ) and ( lc_files_LLE['col1'][i+1] > t_start ):
		    t_start_n = i
	for i in range(len(lc_files_LLE)):
	    if ( lc_files_LLE['col1'][i] <= t_stop ) and ( lc_files_LLE['col1'][i+1] > t_stop ):
		    t_stop_n = i
	print "Start time is: ", t_start_n
	print "Stop time is: ", t_stop_n
	for i in range(len(E_channels_LLE)):
		if ( E_channels_LLE['col1'][i] <= E_start ) and ( E_channels_LLE['col1'][i+1] > E_start ):
			E_start_n = i
	for i in range(len(E_channels_LLE)):
		if ( E_channels_LLE['col1'][i] <= E_stop ) and ( E_channels_LLE['col1'][i+1] > E_stop ):
			E_stop_n = i
	print "Start Energy is: ", E_channels_LLE['col1'][E_start_n]
	print "Stop Energy is: ", E_channels_LLE['col1'][E_stop_n]
	counts = []
	counts_error = []
	for i in range(t_start_n,t_stop_n+1):
		count = 0.0
		err_count = 0.0
		for k in range(E_start_n,E_stop_n):
			p = 4*k+3
			e_p = 4*k+4
			q = 4*k+5
			e_q = 4*k+6
			count = count + lc_files_LLE['col'+str(p)][i]# -lc_files_LLE['col'+str(q)][i]
			x1 = lc_files_LLE['col'+str(e_p)][i]
			x2 = lc_files_LLE['col'+str(e_q)][i]
			err_count=err_count+(x1)**2#+(x2)**2
		print lc_files_LLE['col1'][i], count, np.sqrt(err_count)
		counts.append(count)
		counts_error.append(np.sqrt(err_count))
	counts_array = np.array(counts)
	counts_error_array = np.array(counts_error)
	counts_plt_t = lc_files_LLE['col1'][t_start_n:t_stop_n+1]
	label_pl = str(E_start)+" - "+str(E_stop)+ " keV LAT-LLE"
	return (counts_plt_t,counts_array,counts_error_array,label_pl)



E_BG = [300, 500, 1000, 30000] 
# ~ E_LLE = [20000, 100000] 






	
	
t1 = -50.0
t2 = 450
E = [300, 1000]  


counts_plt_t, counts_array, counts_error_array, label_pl = LC(E[0], E[1], t1, t2)
# ~ counts_plt_t1, counts_array1, counts_error_array1, label_pl1 = LC(E[1], E[2], t1, t2)
# ~ counts_plt_t2, counts_array2, counts_error_array2, label_pl2 = LC(E[2], E[3], t1, t2)
# ~ counts_plt_t_b, counts_array_b, counts_error_array_b, label_pl_b = LCBGO(E_BG[0], E_BG[1], t1, t2)
# ~ counts_plt_t_b1, counts_array_b1, counts_error_array_b1, label_pl_b1 = LCBGO(E_BG[1], E_BG[2], t1, t2)
# ~ counts_plt_t_b2, counts_array_b2, counts_error_array_b2, label_pl_b2 = LCBGO(E_BG[2], E_BG[3], t1, t2)
# ~ counts_plt_t_b3, counts_array_b3, counts_error_array_b3, label_pl_b3 = LCBGO(E_BG[3], E_BG[4], t1, t2)
# ~ counts_plt_t_b4, counts_array_b4, counts_error_array_b4, label_pl_b4 = LCBGO(E_BG[4], E_BG[5], t1, t2)
# ~ counts_plt_t_l, counts_array_l, counts_error_array_l, label_pl_l = LCLLE(E_LLE[0], E_LLE[1], t1, t2)
# ~ counts_plt_t_l1, counts_array_l1, counts_error_array_l1, label_pl_l1 = LCLLE(E_LLE[1], E_LLE[2], t1, t2)

ascii.write([counts_plt_t, counts_array, counts_error_array], 'LC_b1_1s_'+str(E[0])+'-'+str(E[1])+'.qdp', names=['time', 'rate', 'rate_error'], overwrite=True)
# ~ ascii.write([counts_plt_t1, counts_array1, counts_error_array1], 'LC_n6_1s_'+str(E[1])+'-'+str(E[2])+'.qdp', names=['time', 'rate', 'rate_error'], overwrite=True)
# ~ ascii.write([counts_plt_t2, counts_array2, counts_error_array2], 'LC_n6_1s_'+str(E[2])+'-'+str(E[3])+'.qdp', names=['time', 'rate', 'rate_error'], overwrite=True)
# ~ ascii.write([counts_plt_t_b, counts_array_b, counts_error_array_b], 'LC_BG'+str(E_BG[0])+str(E_BG[1])+'.qdp', names=['time', 'rate', 'rate_error'], overwrite=True)
# ~ ascii.write([counts_plt_t_b1, counts_array_b1, counts_error_array_b1], 'LC_BG'+str(E_BG[1])+str(E_BG[2])+'.qdp', names=['time', 'rate', 'rate_error'], overwrite=True)
# ~ ascii.write([counts_plt_t_b2, counts_array_b2, counts_error_array_b2], 'LC_BG'+str(E_BG[2])+str(E_BG[3])+'.qdp', names=['time', 'rate', 'rate_error'], overwrite=True)
# ~ ascii.write([counts_plt_t_b3, counts_array_b3, counts_error_array_b3], 'LC_BG'+str(E_BG[3])+str(E_BG[4])+'.qdp', names=['time', 'rate', 'rate_error'], overwrite=True)
# ~ ascii.write([counts_plt_t_b4, counts_array_b4, counts_error_array_b4], 'LC_BG'+str(E_BG[4])+str(E_BG[5])+'.qdp', names=['time', 'rate', 'rate_error'], overwrite=True)
# ~ ascii.write([counts_plt_t_l, counts_array_l, counts_error_array_l], 'LC_LLE'+str(E_LLE[0])+str(E_LLE[1])+'.qdp', names=['time', 'rate', 'rate_error'], overwrite=True)
# ~ ascii.write([counts_plt_t_l1, counts_array_l1, counts_error_array_l1], 'LC_LLE'+str(E_LLE[1])+str(E_LLE[2])+'.qdp', names=['time', 'rate', 'rate_error'], overwrite=True)
ax1 = plt.subplot(1, 1, 1)
axes = plt.gca()

ax1.plot(counts_plt_t , counts_array ,  '.', lw = 1.25, color='magenta',linestyle='steps-post', label= label_pl,markersize=2, markerfacecolor='none', markeredgecolor='magenta')
plt.legend(numpoints=1,prop={'size':11})


# ~ ax2 = plt.subplot(6, 1, 5, sharex = ax1)
# ~ axes = plt.gca()	
# ~ ax2.plot(counts_plt_t1 , counts_array1 ,  '.', color='magenta',lw = 1.3, linestyle='steps-post', label= label_pl1, markersize=1, markerfacecolor='none', markeredgecolor='magenta')
# ~ plt.legend(numpoints=1,prop={'size':11})
  
# ~ ax3 = plt.subplot(6, 1, 4, sharex = ax1)
# ~ ax3.plot(counts_plt_t_b , counts_array_b ,  '.', color='magenta',lw = 1.3, linestyle='steps-post', label= label_pl_b, markersize=1, markerfacecolor='none', markeredgecolor='magenta')
# ~ plt.legend(numpoints=1,prop={'size':11})
  
# ~ ax4 = plt.subplot(6, 1, 3, sharex = ax1)
# ~ ax4.plot(counts_plt_t_b1  , counts_array_b1  ,  '.', color='magenta',lw = 1.3, linestyle='steps-post', label= label_pl_b1, markersize=1, markerfacecolor='none', markeredgecolor='magenta')
# ~ plt.legend(numpoints=1,prop={'size':11})
  
# ~ ax5 = plt.subplot(6, 1, 2, sharex = ax1)
# ~ ax5.plot(counts_plt_t_l  , counts_array_l  ,  '.', color='magenta',lw = 1.3, linestyle='steps-post', label= label_pl_l, markersize=1, markerfacecolor='none', markeredgecolor='magenta')
# ~ plt.legend(numpoints=1,prop={'size':11})









#~ lc_files_LAT = ascii.read("LAT_HE_2660.txt", header_start = None, data_start=1)
#~ T = np.array([int(lc_files_LAT['col1'][i]) for i in range(len(lc_files_LAT['col1']))])
#~ counts = np.array(lc_files_LAT['col2'])

#~ ax6 = plt.subplot(6, 1, 1, sharex = ax1)
#~ ax6.plot(T, counts, ls='steps-post', ms=6, label= 'LAT > 100 MeV')
#~ ax6.set_xlabel(r'Time($s$)',fontsize=18)
#~ ax6.set_ylabel(r'Counts',fontsize=18)
#~ ax6.set_yscale('log')
#~ ax2.set_xscale('log')

#~ xticklabels = ax2.get_xticklabels() + ax3.get_xticklabels() + ax4.get_xticklabels() + ax5.get_xticklabels() + ax6.get_xticklabels()
#~ plt.setp(xticklabels, visible=False)
plt.subplots_adjust(hspace=0.00)



plt.ylabel(r'Counts $\/$ s$^{-1}$',fontsize= 14 )
plt.legend(numpoints=1,prop={'size':11})
plt.xlabel(r'Time since GBM trigger$\/$(s)',fontsize=14)
plt.subplots_adjust(hspace=0.00)






	
#~ blocks_8_900 = [-1.472, 8, 13, 15, 16, 28, 80]
#~ for i in range(len(blocks_8_900)):
	#~ ax1.axvline(x=blocks_8_900[i], ymin=0.0, linewidth=2.0, color='darkgreen',ls='dashed')
	#~ ax2.axvline(x=blocks_8_900[i], ymin=0.0, linewidth=2.0, color='darkgreen',ls='dashed')
	#~ ax3.axvline(x=blocks_8_900[i], ymin=0.0, linewidth=2.0, color='darkgreen',ls='dashed')
	#~ ax4.axvline(x=blocks_8_900[i], ymin=0.0, linewidth=2.0, color='darkgreen',ls='dashed')
	#~ ax5.axvline(x=blocks_8_900[i], ymin=0.0, linewidth=2.0, color='darkgreen',ls='dashed')
	#~ ax6.axvline(x=blocks_8_900[i], ymin=0.0, linewidth=2.0, color='darkgreen',ls='dashed')
	
plt.show()









