from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal, stats
from scipy.optimize import curve_fit




#Find T90


def t90(tstart, tstop, t, rate):


    # Compute the total source counts
    source_range  = [(t >= tstart) & (t <= tstop)][0]
    
    time_stamps_src_range = t[source_range]

    total_src_counts = np.sum(rate[source_range])
    
    f5 = 0.05*total_src_counts
    f95 = 0.95*total_src_counts
    
    cumulative_sum = np.cumsum(rate[source_range])
    
    
    F90 = [(cumulative_sum  >= f5) & (cumulative_sum <= f95)][0]
    
    t90_stamps = time_stamps_src_range[F90]
    
    T90 = t90_stamps[-1] - t90_stamps[0]


    return T90

	
#error calculation	

def fake_lc(t, rate, rate_err):
	random_nums = np.random.randn(len(t))
	random_signs = random_nums/abs(random_nums)
	
	rate_err_fak = np.random.poisson(rate_err)
	
	rate_fak = rate + random_signs*rate_err_fak
	
	return t, rate_fak, rate_err_fak
	

###########


t = np.linspace(-10, 10, 10000)    
x = 1 + 100*stats.norm.pdf(t, 0, 1)
random_nums = np.random.randn(len(t))
random_signs = random_nums/abs(random_nums)
x1 = x + random_signs*np.random.poisson(np.sqrt(x))
rate = x1
rate_err  = np.random.poisson(np.sqrt(x))
tstart = -3
tstop = 3







nsimulations = 10000

T90_fak = []

for i in range(nsimulations):
	
	fak_lc_t = fake_lc(t, rate, rate_err)[0]
	
	fak_lc_rate = fake_lc(t, rate, rate_err)[1]
	
	find_t90 = t90(tstart, tstop, fak_lc_t, fak_lc_rate)
	
	T90_fak.append(find_t90)
	
	if i%(nsimulations/10) == 0:
		print int(i/(nsimulations/10))*'#' + ' '+str(i/nsimulations*100)+'%'
	else:
		continue


    
    

# from lag distribution find errors in lag

T90_mean = np.mean(T90_fak)
T90_error = np.std(T90_fak)

print 'T90 is: ', T90_mean, '+- ', T90_error


