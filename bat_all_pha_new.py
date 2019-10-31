import os
import math
import scipy
import numpy as np
from astropy.io import ascii
from astropy.io import fits
########################################
print "#Give the ObIds in a text-file"   # Here I put these in 'ObIds' txt file
########################################
def work_dirs(idr_txt):
	ifl = open(idr_txt, "r+")
	idirs_list = ifl.read()
	dirs = [ele for ele in idirs_list.split('\n') if ele != "" if ele != ' ']
	print dirs
	for x in dirs:	
		out_evt_1 = x+"/bat/event_1"
		mk_dir = "mkdir "+out_evt_1
		cp_evt = "cp ./"+x+"/bat/event/*uf* ./"+out_evt_1
		os.system(mk_dir)
		os.system(cp_evt)
	print "Doing: ",dirs
	return dirs	


########################################################################################################################
print "# TO LIST THE FILES IN THE EVENT LIST"
########################################################################################################################
def list_of_event_files(in_dir):   
    LS = "ls "+in_dir+"/bat/event_1/*uf.evt"
    e_names = os.popen(LS)
    e_read = e_names.read() 
    new_list=[]                    
    e_list = [es for es in e_read.split('\n') if es != '']
    #print e_list
    for x in range(0,len(e_list)):
        e_list[x] =e_list[x].strip(in_dir+"/bat/event_1/")+"evt"
    return e_list

print """################################################################
#Step1: Energy Calibration. Tool:bateconvert
#Step2: Crating DPI. Tool:batbinevt'
#Step3: Retrieve Known Problematic Detectors. Tool:batdetmask'
#Step4: Find Noisy Detectors. Tool: bathotpix, total.qmap is quality map'
#Step5: Mask Weighting (Ray Tracing). Tool:batmastevt
################################################################"""
def reduction(ifile, oidn, ras, decs): 
    outdir = oidn+"/bat/event_1/"
    econv = """bateconvert infile= """+outdir+ifile+""" calfile=./"""+str(oidn)+"""/bat/hk/sw"""+str(oidn)+"""bgocb.hk.gz residfile=CALDB pulserfile=CALDB fltpulserfile=CALDB outfile=NONE calmode=INDEF """
    print econv
    os.system(econv)
    dp = "sw"+oidn+"total.dpi"
    dpi_file = """batbinevt infile= """+outdir+ifile+""" outfile= """+outdir+dp+""" outtype=DPI timedel=0 timebinalg=u energybins=15-300 weighted=NO outunits=COUNTS clobber=YES ecol=PI """       
    print dpi_file
    os.system(dpi_file)
    msk0 = "sw"+oidn+"master.mask"
    mask_file = """batdetmask date= """+outdir+dp+""" outfile= """+outdir+msk0+""" clobber=YES detmask=./"""+oidn+"""/bat/hk/sw"""+oidn+"""bdecb.hk.gz """
    msk1 = "sw"+oidn+"master_qmap.mask"
    print mask_file
    os.system(mask_file)
    hot_pix_file = """bathotpix clobber= YES infile= """+outdir+dp+""" outfile= """+outdir+msk1+""" detmask="""+outdir+msk0
    print hot_pix_file
    os.system(hot_pix_file)
    dp = "sw"+oidn+"total.dpi"
    msk1 = "sw"+oidn+"master_qmap.mask"
    print "I AM HERE"
    print "THIS WAS WRONG EARLIER BAT CODES"
    mask_wt_file = """batmastevt infile= """+outdir+ifile+""" attitude=./"""+oidn+"""/auxil/sw"""+oidn+"""sat.fits.gz ra="""+str(ras)+""" dec="""+str(decs)+""" detmask= """+outdir+msk1+""" rebalance=YES corrections=default auxfile=./"""+oidn+"""/bat/event/"""+"""sw"""+oidn+"""bevtr.fits clobber=YES """
    print mask_wt_file
    os.system(mask_wt_file)
#################################################################


#################################################################





    
observations = work_dirs('ObIds')
print observations[0] # Because we have only one ObId so I used index [0]
files =  list_of_event_files(observations[0]) 


print files
number_of_files = len(files) 
if number_of_files > 1:
	print "more than one files"
else:
	print "Only one event file "+files[0]+" is present for "+observations[0]
	



# RA and DEC
GRB_name = 'GRB190829A'

ra = 44.54377
dec = -8.95813

print "######### Time intervals###########"



# Time intervals in a txt file, here "time_intervals"
time_int = ascii.read("swift_tr.txt", header_start = None, data_start=0)
t_a = time_int['col1']
t_b = time_int['col2']
print t_a



print "######## BAT_MET################# \n For analysis with GBM the time corresponding to GBM trigtime is taken" 
oidn = observations[0]
BAT_evt = fits.open(oidn+"/bat/event_1/"+files[0],'readonly')
TRIGTIME = BAT_evt[0].header['TRIGTIME']
BAT_evt.close()
# This is MET of BAT corresponding to GBM trigger time
t0_BAT= TRIGTIME
#~ t0_BAT=465818117.12

time_cuts = np.mean( np.array([t_a,t_b]), axis=0)
print time_cuts
n_time=len(time_cuts)

print time_cuts
print n_time
BAT_t_a = np.array(t0_BAT + t_a)
BAT_t_b = np.array(t0_BAT + t_b)
print BAT_t_a
print BAT_t_b
################################


reduction(files[0], observations[0], ra, dec)

################################


for i in range(0,n_time):
	oidn = observations[0]
	outdir = oidn+"/bat/event_1/"
	ifile = files[0]
	print "#~~~~~~~~~~~~~~~Bin no. "+ str(i+1)+"~~~~~~~~~~~"
	print " "
	print "#Step1: Making the Spectrum. Tool:batbinevt"
	msk1 = "sw"+oidn+"master_qmap.mask"
	pha = "t_BAT_"+str(i+1)+".pha"
	pha_file = """batbinevt detmask= """+outdir+"""sw"""+oidn+"""master_qmap.mask infile= """+outdir+ifile+""" outfile="""+outdir+pha+""" outtype=PHA timedel=0.0 timebinalg=u tstart="""+str(BAT_t_a[i])+""" tstop="""+str(BAT_t_b[i])+""" energybins=CALDB:80 outunits=rate clobber=YES """
	print pha_file
	os.system(pha_file)
	print "#Step2: Corrections. Tool:batupdatepha, batphasyserr"
	com1 = "batupdatepha "+outdir+pha+" auxfile=./"+oidn+"/bat/event/"+"sw"+oidn+"bevtr.fits"
	os.system(com1)
	com2 = "batphasyserr "+outdir+pha+" CALDB"
	os.system(com2)
	print "#Step3: Generate Response Matrix. Tool: batdrmgen"
	com3 = "batdrmgen ./"+outdir+pha+" t_BAT_"+str(i+1)+".rsp NONE clobber=yes"
	os.system(com3)
	mv_rsp = "mv t_BAT_"+str(i+1)+".rsp "+outdir+"t_BAT_"+str(i+1)+".rsp"
	os.system(mv_rsp)
	


# It will make a directory for results and results will be placed in event_1 directory inside it.
mv_results = "mv "+observations[0]+"/bat/event_1 "+observations[0]+"-results_TR"
os.system(mv_results)





	
