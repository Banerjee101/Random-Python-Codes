from __future__ import division
import os
from astropy.io import ascii





GRB_name = 'GRB190114C'
model_name = 'bknpowC'
e_bins = 35


# Read PHA files from an ascii file listed in table
#~ pha_files = ascii.read("pha_file", header_start = None)
#~ print pha_files


# Read models to be used
mod_file = open("model_file_"+model_name, 'r+')
model_list = mod_file.read()
models_to_use = [ele for ele in model_list.split('\n') if ele != '']
mod_file.close()

print '\n'
#print pha_files['col1']
#~ print pha_files['col1'][0]
#~ print pha_files['col2'][0]
#~ t_bins = len(pha_files['col1'])
#~ print "Number of time bins", t_bins


t_bins = 29

print models_to_use
print "Number of models tested ", len(models_to_use)



for i in range(0, t_bins):
    create_xcm_file = "echo \"\" > " + GRB_name +"_"+model_name+"_ind_"+str(i+1)+".xcm"
    os.system(create_xcm_file)
    xcm_file = open(GRB_name+"_"+model_name+"_ind_"+str(i+1)+".xcm", 'r+')
    xcm_file.write("log "+GRB_name+"_"+model_name+"_ind_pgstat"+str(i+1)+".log\n")
    xcm_file.write("lmod grbep ~/Desktop/HEASoft/LocalModels/XspecLocalModels/Band_model\n")
    xcm_file.write("time\n")
    xcm_file.write("query yes\n")
    xcm_file.write("set file1 [open "+GRB_name+"info_fitstat_individual_"+model_name+"_pgstat"+str(i+1)+" w+]\n")
    xcm_file.write("set file2 [open "+GRB_name+"info_fitpar_individual_"+model_name+"_pgstat"+str(i+1)+" w+]\n")
    #~ xcm_file.write("data 1:1 "+ pha_files['col1'][i]+"\n")
    #~ xcm_file.write("data 2:2 "+ pha_files['col2'][i]+"\n")
    #~ xcm_file.write("data 3:3 "+ pha_files['col3'][i]+"\n")
    #~ xcm_file.write("data 4:4 "+ pha_files['col4'][i]+"\n")
    #~ xcm_file.write("data 5:5 "+ pha_files['col5'][i]+"\n")
    xcm_file.write("data 1:1 bn190114873_n3_srcspectra_v01.pha{"+str(i+1)+"}\n")
    xcm_file.write("back 1 bn190114873_n3_bkgspectra.bak{"+str(i+1)+"}\n")
    xcm_file.write("resp 1 bn190114873_n3_weightedrsp.rsp{"+str(i+1)+"}\n")
    xcm_file.write("data 2:2 bn190114873_n4_srcspectra_v01.pha{"+str(i+1)+"}\n")
    xcm_file.write("back 2 bn190114873_n4_bkgspectra.bak{"+str(i+1)+"}\n")
    xcm_file.write("resp 2 bn190114873_n4_weightedrsp.rsp{"+str(i+1)+"}\n")
    xcm_file.write("data 3:3 bn190114873_n7_srcspectra_v01.pha{"+str(i+1)+"}\n")
    xcm_file.write("back 3 bn190114873_n7_bkgspectra.bak{"+str(i+1)+"}\n")
    xcm_file.write("resp 3 bn190114873_n7_weightedrsp.rsp{"+str(i+1)+"}\n")
    # ~ xcm_file.write("data 4:4 bn190114873_n7_srcspectra_v01.pha{"+str(i+1)+"}\n")
    # ~ xcm_file.write("back 4 bn190114873_n7_bkgspectra.bak{"+str(i+1)+"}\n")
    # ~ xcm_file.write("resp 4 bn190114873_n7_weightedrsp.rsp{"+str(i+1)+"}\n")   
    xcm_file.write("data 4:4 bn190114873_b0_srcspectra_v01.pha{"+str(i+1)+"}\n")
    xcm_file.write("back 4 bn190114873_b0_bkgspectra.bak{"+str(i+1)+"}\n")
    xcm_file.write("resp 4 bn190114873_b0_weightedrsp.rsp{"+str(i+1)+"}\n")
    xcm_file.write("data 5:5 bn190114873_b1_srcspectra_v01.pha{"+str(i+1)+"}\n")
    xcm_file.write("back 5 bn190114873_b1_bkgspectra.bak{"+str(i+1)+"}\n")
    xcm_file.write("resp 5 bn190114873_b1_weightedrsp.rsp{"+str(i+1)+"}\n")
    # ~ if i < 10:
        # ~ xcm_file.write("@loadData_bn190114873_int0"+str(i+1)+".xcm\n")
    # ~ else:
        # ~ xcm_file.write("@loadData_bn190114873_int"+str(i+1)+".xcm\n")


    #~ xcm_file.write("@loadData_bn160509374_int0"+str(i+1)+".xcm\n")
    #~ xcm_file.write("ign 1:1-4,125-128 2:1-5,125-128 3:1-5,125-128 4:1-4,120-128 5:1-8,17-50 \n")
    xcm_file.write("ign 1-3: **-8.0 25.0-40.0 900.0-**\n")
    # ~ xcm_file.write("ign 1-4: 25.0-40.0\n")
    xcm_file.write("ign 4-5: **-200.0 38000.0-**\n")
    #~ xcm_file.write("ign 5:5 **-20000.0 100000.0-**\n")
    xcm_file.write("setp ene\n")
    #~ xcm_file.write("method leven 500 0.01\n")
    xcm_file.write("abund angr\n")
    xcm_file.write("xsect bcmc\n")
    xcm_file.write("cosmo 70 0 0.73\n")
    xcm_file.write("xset delta 0.01\n")
    xcm_file.write("systematic 0\n")
    xcm_file.write("ignore bad\n")
    xcm_file.write("mo cons*("+models_to_use[0]+")\n")
    initial_values = open("init_"+model_name+"", 'r+')
    xcm_file.write(initial_values.read())
    initial_values.close()
    initial_values1 = open("init_"+model_name+"", 'r+')
    initial_values_list = initial_values1.read()
    lines_num = e_bins
    initial_values1.close()
    xcm_file.write("renorm\n")
    #~ xcm_file.write("statistic chi\n")
    #~ xcm_file.write("fit 500\n")
    xcm_file.write("statistic pgstat\n")
    xcm_file.write("cpd /xw\n")
    xcm_file.write("pl eeufsp de\n")
    xcm_file.write("parallel leven 4\n")
    xcm_file.write("parallel error 4\n")
    xcm_file.write("fit 500\n")
    xcm_file.write("fit 500\n")
    xcm_file.write("error 1-"+str(e_bins)+"\n")
    xcm_file.write("fit 500\n")
    xcm_file.write("fit 500\n")
    xcm_file.write("error 1-"+str(e_bins)+"\n")
    #~ xcm_file.write("fit \n")
    #~ xcm_file.write("fit \n")
    xcm_file.write("flux 10.0 1000.0 err\n")
    xcm_file.write("set pgst [tcloutr stat]\n")
    xcm_file.write("tclout dof\n")
    xcm_file.write("set dof [lindex $xspec_tclout 0]\n")
    xcm_file.write("tclout flux 1\n")
    xcm_file.write("set flu [lindex $xspec_tclout 0]\n")
    xcm_file.write("set f1 [lindex $xspec_tclout 1]\n")
    xcm_file.write("set f2 [lindex $xspec_tclout 2]\n")
    xcm_file.write("set phot [lindex $xspec_tclout 3]\n")
    xcm_file.write("set ph1 [lindex $xspec_tclout 4]\n")
    xcm_file.write("set ph2 [lindex $xspec_tclout 5]\n")
    #~ xcm_file.write("set rchi [expr ($chisq)/($dof)]\n")
    #~ xcm_file.write("if {$rchi < 2} {error 1-11}\n")
    #~ xcm_file.write("error 1-11\n")
    xcm_file.write("cpd /xw\n")
    xcm_file.write("pl d del\n")
    xcm_file.write("cpd "+GRB_name+"_"+model_name+"_ind_"+str(i+1)+".ps/cps\n")
    #xcm_file.write("pl uf del\n")
    #xcm_file.write("pl euf del\n")
    xcm_file.write("setp rebin 5 5\n")
    #~ xcm_file.write("pl eeuf res\n")
    xcm_file.write("pl eeuf del\n")
    xcm_file.write("cpd none\n")
    xcm_file.write("set model [tcloutr model]\n")  
    xcm_file.write("set pgst [tcloutr stat]\n")
    xcm_file.write("tclout dof\n")
    xcm_file.write("set dof [lindex $xspec_tclout 0]\n")
    #~ xcm_file.write("set rchi [expr ($chisq)/($dof)]\n")
    xcm_file.write("puts $file1 \""+str(i+1) +" [lindex $pgst]   [lindex $dof]\"\n")
    z_arr=''
    for j in range(1, int(lines_num) + 1):
		xcm_file.write("tclout param "+str(j)+"\n")
		xcm_file.write("set par"+str(j)+" [lindex $xspec_tclout 0]\n")
		xcm_file.write("set parstat"+str(j)+" [lindex $xspec_tclout 1]\n")
		xcm_file.write("tclout error "+str(j)+"\n")
		xcm_file.write("set par"+str(j)+"err1"+" [lindex $xspec_tclout 0]\n")
		xcm_file.write("set par"+str(j)+"err2"+" [lindex $xspec_tclout 1]\n")
		xcm_file.write("set l"+str(j)+" [expr $par"+str(j)+"err1-$par"+str(j)+"]\n")
		xcm_file.write("set u"+str(j)+" [expr $par"+str(j)+"err2-$par"+str(j)+"]\n")
		z_arr=z_arr+" [lindex $par"+str(j)+"] [lindex $l"+str(j)+"] [lindex $u"+str(j)+"]"
    # The following will be used only when there are more then one componet and to calculate flux of a mode by setting norm of others to zero
    #~ xcm_file.write("new 6 0.0\n")
    #~ xcm_file.write("freeze 6\n")
    #~ xcm_file.write("flux 8.0 100000.0 err\n")  # to get flux of 2nd component freeze norm of 1st and 3rd to zero
    #~ xcm_file.write("tclout flux 3\n")
    #~ xcm_file.write("set fluz [lindex $xspec_tclout 0]\n")  
    #~ xcm_file.write("set fz1 [lindex $xspec_tclout 1]\n")
    #~ xcm_file.write("set fz2 [lindex $xspec_tclout 2]\n")
    #~ xcm_file.write("set photz [lindex $xspec_tclout 3]\n")
    #~ xcm_file.write("set phz1 [lindex $xspec_tclout 4]\n")
    #~ xcm_file.write("set phz2 [lindex $xspec_tclout 5]\n")
    #~ xcm_file.write("new 8 0.0\n")
    #~ xcm_file.write("freeze 8\n")
    #~ xcm_file.write("flux 8.0 100000.0 err\n")
    #~ xcm_file.write("tclout flux 3\n")
    #~ xcm_file.write("set fluzz [lindex $xspec_tclout 0]\n")  
    #~ xcm_file.write("set fzz1 [lindex $xspec_tclout 1]\n")
    #~ xcm_file.write("set fzz2 [lindex $xspec_tclout 2]\n")
    #~ xcm_file.write("set photzz [lindex $xspec_tclout 3]\n")
    #~ xcm_file.write("set phzz1 [lindex $xspec_tclout 4]\n")
    #~ xcm_file.write("set phzz2 [lindex $xspec_tclout 5]\n")
    z_arr="puts $file2 \""+z_arr+" [lindex $flu] [lindex $f1] [lindex $f2] [lindex $phot] [lindex $ph1] [lindex $ph2] \""#[lindex $fluz] [lindex $fz1] [lindex $fz2] [lindex $photz] [lindex $phz1] [lindex $phz2] [lindex $fluzz] [lindex $fzz1] [lindex $fzz2] [lindex $photzz] [lindex $phzz1] [lindex $phzz2]\""
    xcm_file.write(z_arr+"\n")
    xcm_file.write("log none\n")
    xcm_file.write("time\n")
    xcm_file.write("close $file1\n")
    xcm_file.write("close $file2\n")
    xcm_file.write("log none $file2\n")
    xcm_file.write("quit $file2\n")
    xcm_file.write("\n")
    xcm_file.close()




