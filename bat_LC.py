import os
import math
import scipy
import numpy as np
from astropy.io import ascii
from astropy.io import fits
########################################
print "#Give the ObIds in a text-file"
########################################
def work_dirs(idr_txt):
	ifl = open(idr_txt, "r+")
	idirs_list = ifl.read()
	dirs = [ele for ele in idirs_list.split('\n') if ele != "" if ele != ' ']
	print dirs
	for x in dirs:	
		out_evt_1 = x+"/bat/event_2"
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
    LS = "ls "+in_dir+"/bat/event_2/*uf.evt"
    e_names = os.popen(LS)
    e_read = e_names.read() 
    new_list=[]                    
    e_list = [es for es in e_read.split('\n') if es != '']
    #print e_list
    for x in range(0,len(e_list)):
        e_list[x] =e_list[x].strip(in_dir+"/bat/event_2/")+"evt"
    return e_list

print """################################################################
#Step1: Energy Calibration. Tool:bateconvert
#Step2: Crating DPI. Tool:batbinevt'
#Step3: Retrieve Known Problematic Detectors. Tool:batdetmask'
#Step4: Find Noisy Detectors. Tool: bathotpix, total.qmap is quality map'
#Step5: Mask Weighting (Ray Tracing). Tool:batmastevt
################################################################"""
def reduction(ifile, oidn, ras, decs): 
    outdir = oidn+"/bat/event_2/"
    econv = """bateconvert infile= """+outdir+ifile+""" calfile=./"""+str(oidn)+"""/bat/hk/sw"""+str(oidn)+"""bgocb.hk.gz residfile=CALDB pulserfile=CALDB fltpulserfile=CALDB outfile=NONE calmode=INDEF """
    print econv
    os.system(econv)
    dp = "sw"+oidn+"total.dpi"
    dpi_file = """batbinevt infile= """+outdir+ifile+""" outfile= """+outdir+dp+""" outtype=DPI timedel=0 timebinalg=u energybins=15-300 weighted=NO outunits=COUNTS clobber=YES ecol=PI """       
    print dpi_file
    os.system(dpi_file)
    msk0 = "sw"+oidn+"master.mask"
    mask_file = """batdetmask date= """+outdir+dp+""" outfile="""+outdir+msk0+""" clobber=YES detmask=./"""+oidn+"""/bat/hk/sw"""+oidn+"""bdecb.hk.gz """
    msk1 = "sw"+oidn+"master_qmap.mask"
    print mask_file
    os.system(mask_file)
    hot_pix_file = """bathotpix clobber= YES infile= """+outdir+dp+""" outfile= """+outdir+msk1+""" detmask="""+outdir+msk0
    print hot_pix_file
    os.system(hot_pix_file)
    mask_wt_file = """batmastevt infile= """+outdir+ifile+""" attitude=./"""+oidn+"""/auxil/sw"""+oidn+"""sat.fits.gz ra="""+str(ras)+""" dec="""+str(decs)+""" detmask= """+outdir+msk1+""" rebalance=YES corrections=default auxfile=./"""+oidn+"""/bat/event/"""+"""sw"""+oidn+"""bevtr.fits clobber=YES """
    os.system(mask_wt_file)
#################################################################
#################################################################
    
def l_curve(ifile,oidn,l, e_b, START, STOP): 
    outdir = oidn+"/bat/event_2/"
    lc = "BAT_"+l+"_"+e_b+".lc"
    lc_file = """batbinevt detmask= """+outdir+"""sw"""+oidn+"""master_qmap.mask infile= """+outdir+ifile+""" outfile="""+outdir+lc+""" \
              outtype=LC timedel="""+l+""" timebinalg=u energybins="""+e_b+""" tstart= """+str(START)+""" tstop= """+str(STOP)+""" \
              weighted=YES clobber=YES """       
    print lc_file
    os.system(lc_file)

################################################################# 
#################################################################
def f_plot(ifl, oidn, l, e_b):
    lc_file = "BAT_"+l+"_"+e_b+".lc"
    flc_file = "BAT_"+l+"_"+e_b+"_v1.lc"
    outdir = oidn+"/bat/event_2/"
    f_clc = """fcalc """+outdir+lc_file +""" """+ outdir+flc_file+""" TIME \"TIME-TRIGTIME\" """
    os.system(f_clc)
    print outdir+lc_file
    fplot_cmd = """fplot infile= """+outdir+flc_file+""" xparm=TIME yparm=RATE[ERROR] device= """+outdir+"""\"sw"""+oidn+"""_"""+l+"""sec_"""+e_b+"""_lc.ps/ps\" pltcmd=@plt_cmd.pco rows=- offset=no"""
    print fplot_cmd
    os.system(fplot_cmd)
    ps_pdf = """ps2pdf """+outdir+"""sw"""+oidn+"""_"""+l+"""sec_"""+e_b+"""_lc.ps """+outdir+"""sw"""+oidn+"""_"""+l+"""sec_"""+e_b+"""_lc.pdf"""
    print ps_pdf
    os.system(ps_pdf)


    
observations = work_dirs('ObIds')
print observations[0]
files =  list_of_event_files(observations[0]) 

print files
number_of_files = len(files) 
if number_of_files > 1:
	print "more than one files"
else:
	print "Only one event file "+files[0]+" is present for "+observations[0]
	






print "######### RA and DEC###########"

ra=44.54377
dec=-8.95813
TSTART = -100
TSTOP = 200
#====================================
reduction(files[0], observations[0], ra, dec)

oidn = observations[0]
BAT_evt = fits.open(oidn+"/bat/event_2/"+files[0],'readonly')
TRIGTIME = BAT_evt[0].header['TRIGTIME']
# ~ TSTART = BAT_evt[0].header['TSTART']
# ~ TSTOP = BAT_evt[0].header['TSTOP']
TSTART = TSTART  + TRIGTIME
TSTOP =  TSTOP + TRIGTIME
BAT_evt.close()
################################

E_b = ["15-150"]
for e in E_b:
	oidn = observations[0]
	outdir = oidn+"/bat/event_2/"
	ifile = files[0]
	print "lcurve for energy range "+e+" \n"
	print " "
	print "#Step1: Making the Light curve. Tool:batbinevt"
	msk1 = "sw"+oidn+"master_qmap.mask"
	l_curve(ifile,oidn,"1", e, TSTART, TSTOP)
	print "#Step2: Ploting the lightcurve. Tool:fplot"
	f_plot(ifile, oidn, "1",e)
	



mv_results = "mv "+observations[0]+"/bat/event_2 "+observations[0]+"-resultsLC_1s"
mv_lc = "mv BAT_LC.qdp "+observations[0]+"-resultsLC_1s"
mv_pco = "mv BAT_LC.pco "+observations[0]+"-resultsLC_1s"
os.system(mv_results)
os.system(mv_lc)
os.system(mv_pco)



	
