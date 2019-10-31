import os
import math
import scipy
import numpy as np
from astropy.io import ascii
from astropy.io import fits
import matplotlib.pyplot as plt
import matplotlib as mpl
########################################
#~ print "#Give the ObIds in a text-file"
#~ font = {
        #~ 'weight' : 'bold',
        #~ 'size'   : 15}

#~ mpl.rc('font', **font)
#~ mpl.rcParams['axes.linewidth'] = 1.5
#~ mpl.rcParams['axes.labelweight']='bold'
#~ mpl.rcParams['axes.labelsize']='large'
#~ mpl.rcParams['xtick.major.size'] = 4
#~ mpl.rcParams['xtick.major.width'] = 2
#~ mpl.rcParams['ytick.major.size'] = 4
#~ mpl.rcParams['ytick.major.width'] = 2



BAT_LC_data = ascii.read("BAT_LC.qdp", header_start = None, data_start=3)


time_cen = np.array(BAT_LC_data['col1'])
#~ start_times =np.array(BAT_LC_data['col2'])
#~ stop_times =np.array(BAT_LC_data['col3'])
rate_bins =np.array(BAT_LC_data['col2'])
rate_errors =np.array(BAT_LC_data['col3'])

plt.plot(time_cen, rate_bins, '.', color='grey',linestyle='steps-post',markersize=0, markerfacecolor='none', markeredgecolor='grey',lw = 1.0)


# ~ BAT_snr30_bins = ascii.read("BAT_LC_times_snr30.qdp", header_start = None, data_start=0, comment = '#')
# ~ t_mid = BAT_snr30_bins['col1']
# ~ t_s = BAT_snr30_bins['col2']
# ~ t_stop = BAT_snr30_bins['col3']
# ~ rate_bat = BAT_snr30_bins['col4']
# ~ rate_bat_err = BAT_snr30_bins['col5']

#~ last = t_stop
# ~ plt.plot(t_s, rate_bat, '.', color='k',linestyle='steps-post',markersize=0, markerfacecolor='none', markeredgecolor='grey',lw = 1.5)
#~ plt.plot(t_s, rate_bat, yerr=rate_bat_err, fmt='.', color='k',lw = 1.3, markersize=0, linestyle='steps-post', markerfacecolor='none', markeredgecolor='k')
plt.axvline(x=-52.1144, ymin=-10, ymax=10000,ls='dotted')
plt.axvline(x=-43.4104, ymin=-10, ymax=10000,ls='dotted')
plt.axvline(x=-4.4344, ymin=-10, ymax=10000,ls='dotted')
plt.axvline(x=10.9896, ymin=-10, ymax=10000,ls='dotted')
plt.axvline(x=t_stop[-2], ymin=-10, ymax=10000,ls='dotted')

plt.ylabel(r'Counts $\/$ s$^{-1}$ det$^{-1}$',fontsize= 14 )
#~ plt.legend(numpoints=1,prop={'size':11})
plt.xlabel(r'Time since BAT trigger$\/$(s)',fontsize=14)
plt.show()

