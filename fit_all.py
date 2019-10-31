
from __future__ import division
import os
from astropy.io import ascii

data_sequence = 'all'
GRB_name = 'GRB190114C'
model_name = 'CPL+BB_'+data_sequence						#change if you want to change the time pulse bin, also change if you change the SNR

# Read PHA files from an ascii file listed in table
pha_files = ascii.read("Pulse1_"+data_sequence+"_list", header_start = None)
print (pha_files)


# Read models to be used
mod_file = open("model_file_"+model_name, 'r+')
model_list = mod_file.read()
models_to_use = [ele for ele in model_list.split('\n') if ele != '']
mod_file.close()

print ('\n')
#print pha_files['col1']
print (pha_files['col1'][0])
print (pha_files['col2'][0])
t_bins = len(pha_files['col1'])
print ("Number of time bins", t_bins)

print (models_to_use)
print ("Number of models tested ", len(models_to_use))

create_xspec_file = "echo \"\" > " + "xspec_fit_v3_"+model_name+".xcm"
os.system(create_xspec_file)
xcm_file = open("xspec_fit_v3_"+model_name+".xcm", 'r+')
xcm_file.write("lmod grbep /home/ankush/Desktop/HEASoft/LocalModels/XspecLocalModels/Band_model\n")
xcm_file.write("time\n")
xcm_file.write("query yes\n")
xcm_file.write("set file1 [open "+GRB_name+"info_fitstat_"+model_name+" w+]\n")
xcm_file.write("set file2 [open "+GRB_name+"info_fitpar_"+model_name+" w+]\n")
for i in range(0, t_bins):
    xcm_file.write("log "+GRB_name+"_"+model_name+"_pha"+str(i+1)+".log\n")
    xcm_file.write("data 1:1 "+pha_files['col1'][i]+"\n")
    xcm_file.write("data 2:2 "+pha_files['col2'][i]+"\n")
    xcm_file.write("data 3:3 "+pha_files['col3'][i]+"\n")
    xcm_file.write("data 4:4 "+pha_files['col4'][i]+"\n")
    xcm_file.write("data 5:5 "+pha_files['col5'][i]+"\n")
    xcm_file.write("setp ene\n")
    #~ xcm_file.write("setp rebin 5 5\n")
    xcm_file.write("ign 1-3: **-8.0 900.0-**\n")
    xcm_file.write("ig 1-3: 25.0-40.0\n")
    xcm_file.write("ign 4-5: **-200.0 40000.0-**\n")
    #xcm_file.write("ign 5: **-15.0 150.0-**\n")
    xcm_file.write("mo cons*("+models_to_use[0]+")\n")
    initial_values = open("init_"+model_name, 'r+')						
    xcm_file.write(initial_values.read())
    initial_values.close()
    initial_values1 = open("init_"+model_name, 'r+')
    initial_values_list = initial_values1.read()
    nlines = [ele for ele in initial_values_list.split('\n') if ele != '']
    lines_num = len(nlines)
    initial_values1.close()
    xcm_file.write("statistic pgstat\n")
    xcm_file.write("setplot rebin 5 5\n")
    xcm_file.write("fit 500\n")
    xcm_file.write("fit 500\n")
    xcm_file.write("err 1-"+str(lines_num)+"\n")
    #xcm_file.write("flux 8.0 40000.0 err\n")
    xcm_file.write("set chisq [tcloutr stat]\n")
    xcm_file.write("tclout dof\n")
    xcm_file.write("set dof [lindex $xspec_tclout 0]\n")
    xcm_file.write("tclout flux 2\n")
    xcm_file.write("set flu [lindex $xspec_tclout 0]\n")
    xcm_file.write("set f1 [lindex $xspec_tclout 1]\n")
    xcm_file.write("set f2 [lindex $xspec_tclout 2]\n")
    xcm_file.write("set phot [lindex $xspec_tclout 3]\n")
    xcm_file.write("set ph1 [lindex $xspec_tclout 4]\n")
    xcm_file.write("set ph2 [lindex $xspec_tclout 5]\n")
    xcm_file.write("set rchi [expr ($chisq)/($dof)]\n")
    xcm_file.write("if {$rchi < 2} {error 1-"+str(lines_num)+"}\n")
    xcm_file.write("cpd /xw\n")
    xcm_file.write("pl d del\n")
    xcm_file.write("cpd individual_pha_"+model_name+"_"+str(i+1)+".ps/cps\n")
    #xcm_file.write("pl uf del\n")
    #xcm_file.write("pl euf del\n")
    xcm_file.write("pl eeuf del\n")
    xcm_file.write("cpd none\n")
    xcm_file.write("set model [tcloutr model]\n")  
    xcm_file.write("set chisq [tcloutr stat]\n")
    xcm_file.write("tclout dof\n")
    xcm_file.write("set dof [lindex $xspec_tclout 0]\n")
    xcm_file.write("set rchi [expr ($chisq)/($dof)]\n")
    xcm_file.write("puts $file1 \""+str(i+1) +" [lindex $rchi] [lindex $chisq]  [lindex $dof]\"\n")
    z_arr=''
    for j in range(1, int(lines_num/5) + 2):
		xcm_file.write("tclout param "+str(j)+"\n")
		xcm_file.write("set par"+str(j)+" [lindex $xspec_tclout 0]\n")
		xcm_file.write("set parstat"+str(j)+" [lindex $xspec_tclout 1]\n")
		xcm_file.write("tclout error "+str(j)+"\n")
		xcm_file.write("set par"+str(j)+"err1"+" [lindex $xspec_tclout 0]\n")
		xcm_file.write("set par"+str(j)+"err2"+" [lindex $xspec_tclout 1]\n")
		xcm_file.write("set l"+str(j)+" [expr $par"+str(j)+"err1-$par"+str(j)+"]\n")
		xcm_file.write("set u"+str(j)+" [expr $par"+str(j)+"err2-$par"+str(j)+"]\n")
		z_arr=z_arr+" [lindex $par"+str(j)+"] [lindex $l"+str(j)+"] [lindex $u"+str(j)+"]"
    #xcm_file.write("new 7 0.0\n")
    xcm_file.write("freeze 3\n")
    xcm_file.write("flux 8.0 900.0 err\n")
    xcm_file.write("tclout flux 2\n")
    xcm_file.write("set fluz [lindex $xspec_tclout 0]\n")  
    xcm_file.write("set fz1 [lindex $xspec_tclout 1]\n")
    xcm_file.write("set fz2 [lindex $xspec_tclout 2]\n")
    xcm_file.write("set photz [lindex $xspec_tclout 3]\n")
    xcm_file.write("set phz1 [lindex $xspec_tclout 4]\n")
    xcm_file.write("set phz2 [lindex $xspec_tclout 5]\n")
    #xcm_file.write("new 5 0.0\n")
    xcm_file.write("freeze 3\n")
    xcm_file.write("flux 8.0 900.0 err\n")						#Change if you want to change the flux energy range
    xcm_file.write("tclout flux 2\n")
    xcm_file.write("set fluzz [lindex $xspec_tclout 0]\n")  
    xcm_file.write("set fzz1 [lindex $xspec_tclout 1]\n")
    xcm_file.write("set fzz2 [lindex $xspec_tclout 2]\n")
    xcm_file.write("set photzz [lindex $xspec_tclout 3]\n")
    xcm_file.write("set phzz1 [lindex $xspec_tclout 4]\n")
    xcm_file.write("set phzz2 [lindex $xspec_tclout 5]\n")
    z_arr="puts $file2 \""+z_arr+" [lindex $flu] [lindex $f1] [lindex $f2] [lindex $phot] [lindex $ph1] [lindex $ph2] [lindex $fluz] [lindex $fz1] [lindex $fz2] [lindex $photz] [lindex $phz1] [lindex $phz2] [lindex $fluzz] [lindex $fzz1] [lindex $fzz2] [lindex $photzz] [lindex $phzz1] [lindex $phzz2]\""
    xcm_file.write(z_arr+"\n")
    xcm_file.write("log none\n")
    xcm_file.write("time\n")
xcm_file.write("close $file1\n")
xcm_file.write("close $file2\n")
xcm_file.close()




