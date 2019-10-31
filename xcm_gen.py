
from __future__ import division
import os
from astropy.io import ascii

# ~ data_sequence = 'all'
# ~ GRB_name = 'GRB190114C'
# ~ model_name = 'CPL+BB_'+data_sequence						#change if you want to change the time pulse bin, also change if you change the SNR

# Read PHA files from an ascii file listed in table
# ~ pha_files = ascii.read("Pulse1_"+data_sequence+"_list", header_start = None)
# ~ print (pha_files)

# Read models to be used
# ~ mod_file = open("model_file_"+model_name, 'r+')
# ~ model_list = mod_file.read()
# ~ models_to_use = [ele for ele in model_list.split('\n') if ele != '']
# ~ mod_file.close()

#This program will just generate a text file which you are supposed to copy and paste in the xspec terminal to achieve fitting. 
#Written in a hurry


model_name = 'BB_Band_'				#Change this for any other model
Seq = 36										#Enter the number of time bins yew need
for i in range(1, Seq+1):
	Seq_no = i
	create_xspec_file = "echo \"\" > " + "xspec_seq"+str(Seq_no)+"_v1_"+model_name+".txt"
	os.system(create_xspec_file)
	xcm_file = open("xspec_seq"+str(Seq_no)+"_v1_"+model_name+".txt", 'r+')
	xcm_file.write("log LRT1_BB_Band"+str(Seq_no)+".log\n")
	xcm_file.write("grppha\n")
	xcm_file.write("n3_src"+str(Seq_no)+".pha\n")
	xcm_file.write("n3_src"+str(Seq_no)+"_grp20.pha\n")
	xcm_file.write("group min 20\n")
	xcm_file.write("exit\n")
	xcm_file.write("grppha\n")
	xcm_file.write("n4_src"+str(Seq_no)+".pha\n")
	xcm_file.write("n4_src"+str(Seq_no)+"_grp20.pha\n")
	xcm_file.write("group min 20\n")
	xcm_file.write("exit\n")
	xcm_file.write("grppha\n")
	xcm_file.write("n8_src"+str(Seq_no)+".pha\n")
	xcm_file.write("n8_src"+str(Seq_no)+"_grp20.pha\n")
	xcm_file.write("group min 20\n")
	xcm_file.write("exit\n")
	xcm_file.write("grppha\n")
	xcm_file.write("b0_src"+str(Seq_no)+".pha\n")
	xcm_file.write("b0_src"+str(Seq_no)+"_grp20.pha\n")
	xcm_file.write("group min 20\n")
	xcm_file.write("exit\n")
	xcm_file.write("grppha\n")
	xcm_file.write("b1_src"+str(Seq_no)+".pha\n")
	xcm_file.write("b1_src"+str(Seq_no)+"_grp20.pha\n")
	xcm_file.write("group min 20\n")
	xcm_file.write("exit\n")
	xcm_file.write("data 1:1 n3_src"+str(Seq_no)+"_grp20.pha \n")
	xcm_file.write("back 1 n3_bak"+str(Seq_no)+".bak \n")
	xcm_file.write("resp 1 glg_cspec_n3_bn190114873_v02.rsp\n")
	xcm_file.write("data 2:2 n4_src"+str(Seq_no)+"_grp20.pha \n")
	xcm_file.write("back 2 n4_bak"+str(Seq_no)+".bak \n")
	xcm_file.write("resp 2 glg_cspec_n4_bn190114873_v02.rsp\n")
	xcm_file.write("data 3:3 n8_src"+str(Seq_no)+"_grp20.pha \n")
	xcm_file.write("back 3 n8_bak"+str(Seq_no)+".bak \n")
	xcm_file.write("resp 3 glg_cspec_n8_bn190114873_v02.rsp\n")
	xcm_file.write("data 4:4 b1_src"+str(Seq_no)+"_grp20.pha \n")
	xcm_file.write("back 4 b1_bak"+str(Seq_no)+".bak \n")
	xcm_file.write("resp 4 glg_cspec_b1_bn190114873_v02.rsp\n")
	xcm_file.write("setplot energy\n")
	xcm_file.write("query yes\n")
	xcm_file.write("ig 1-3: **-8.0 400.0-**\n")
	xcm_file.write("ig 1-3: 25.0-40.0\n")
	xcm_file.write("ig 4-5: **-200.0 40000.0-**\n")
	xcm_file.write("ignore bad\n")
	xcm_file.write("statistic pgstat\n")
	xcm_file.write("lmod grbep ~/Desktop/HEASoft/LocalModels/XspecLocalModels/Band_model\n")
	xcm_file.write("model  constant(bbody + ngrbep)\n")													#Change this and the following lines as per the model fitting parameters as need be
	xcm_file.write("              1         -1          0          0      1e+10      1e+10\n")
	xcm_file.write("        33.1348          5         10         10        100        100\n")
	xcm_file.write("        1.41026       0.01          0          0      1e+20      1e+24\n")
	xcm_file.write("      -0.855125       0.01        -10         -3          2          5\n")
	xcm_file.write("       -3.69342       0.01        -10         -5          2         10\n")
	xcm_file.write("        472.566         10        0.1        0.1       1000      10000\n")
	xcm_file.write("            100      -0.01          0          0       1000       1000\n")
	xcm_file.write("       0.142905       0.01          0          0      1e+20      1e+24\n")
	xcm_file.write("           1.05         -1          0          0      1e+10      1e+10\n")
	xcm_file.write("= p2\n")
	xcm_file.write("= p3\n")
	xcm_file.write("= p4\n")
	xcm_file.write("= p5\n")
	xcm_file.write("= p6\n")
	xcm_file.write("= p7\n")
	xcm_file.write("= p8\n")
	xcm_file.write("           1.15         -1          0          0      1e+10      1e+10\n")
	xcm_file.write("= p2\n")
	xcm_file.write("= p3\n")
	xcm_file.write("= p4\n")
	xcm_file.write("= p5\n")
	xcm_file.write("= p6\n")
	xcm_file.write("= p7\n")
	xcm_file.write("= p8\n")
	xcm_file.write("           1.09         -1          0          0      1e+10      1e+10\n")
	xcm_file.write("= p2\n")
	xcm_file.write("= p3\n")
	xcm_file.write("= p4\n")
	xcm_file.write("= p5\n")
	xcm_file.write("= p6\n")
	xcm_file.write("= p7\n")
	xcm_file.write("= p8\n")																			#Change till here
	xcm_file.write("fit\n")
	xcm_file.write("error 1-32\n")
	xcm_file.write("fit\n")
	xcm_file.write("cpd /xw\n")
	xcm_file.write("pl eeufspec del\n")
	xcm_file.write("ipl\n")
	xcm_file.write("we BB_Band"+str(Seq_no)+".qdp\n")
	xcm_file.write("cpd BB_Band"+str(Seq_no)+".eps/cps\n")
	xcm_file.write("pl\n")
	xcm_file.write("cpd /xw\n")
	xcm_file.write("pl\n")
	xcm_file.write("q\n")
	xcm_file.write("save model BB_Band"+str(Seq_no)+".xcm\n")
	xcm_file.write("simftest 2 30000 simftest2_"+str(Seq_no)+"_1\n")
	xcm_file.close()
	
