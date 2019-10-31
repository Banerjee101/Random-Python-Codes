
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


model_name = 'BB+CPL'				#Change this for any other model
Seq = 36										#Enter the number of time bins yew need
for i in range(1, Seq+1):
	Seq_no = i
	create_xspec_file = "echo \"\" > " + "xspec_seq"+str(Seq_no)+"_v1_"+model_name+".txt"
	os.system(create_xspec_file)
	xcm_file = open("xspec_seq"+str(Seq_no)+"_v1_"+model_name+".txt", 'r+')
	xcm_file.write("log Band_"+str(Seq_no)+".log\n")
	xcm_file.write("data 1:1 n3_src"+str(Seq_no)+".pha \n")
	xcm_file.write("back 1 n3_bak"+str(Seq_no)+".bak \n")
	xcm_file.write("resp 1 bn190114873_n3_weightedrsp.rsp\n")
	xcm_file.write("data 2:2 n4_src"+str(Seq_no)+".pha \n")
	xcm_file.write("back 2 n4_bak"+str(Seq_no)+".bak \n")
	xcm_file.write("resp 2 bn190114873_n4_weightedrsp.rsp\n")
	xcm_file.write("data 3:3 n7_src"+str(Seq_no)+".pha \n")
	xcm_file.write("back 3 n7_bak"+str(Seq_no)+".bak \n")
	xcm_file.write("resp 3 bn190114873_n7_weightedrsp.rsp\n")
	#xcm_file.write("data 4:4 n8_src"+str(Seq_no)+".pha \n")
	#xcm_file.write("back 4 n8_bak"+str(Seq_no)+".bak \n")
	#xcm_file.write("resp 4 bn190114873_n8_weightedrsp.rsp\n")
	xcm_file.write("data 5:5 b0_src"+str(Seq_no)+".pha \n")
	xcm_file.write("back 5 b0_bak"+str(Seq_no)+".bak \n")
	xcm_file.write("resp 5 bn190114873_b0_weightedrsp.rsp\n")
	xcm_file.write("data 6:6 b1_src"+str(Seq_no)+".pha \n")
	xcm_file.write("back 6 b1_bak"+str(Seq_no)+".bak \n")
	xcm_file.write("resp 6 bn190114873_b1_weightedrsp.rsp\n")
	xcm_file.write("setplot energy\n")
	xcm_file.write("statistic pgstat\n")
	xcm_file.write("query yes\n")
	xcm_file.write("ig 1-4: **-8.0 900.0-**\n")
	xcm_file.write("ig 1-4: 25.0-40.0\n")
	xcm_file.write("ig 5-6: **-200.0 38000.0-**\n")
	xcm_file.write("ignore bad\n")
	xcm_file.write("lmod grbep ~/Desktop/HEASoft/LocalModels/XspecLocalModels/Band_model\n")
	xcm_file.write("mo const*(bbody+cutoffpl) \n")
	xcm_file.write("1 -1\n")
	xcm_file.write("/*\n")
	xcm_file.write("fit\n")
	xcm_file.write("cpd /xw\n")
	xcm_file.write("pl eeufspec del\n")
	xcm_file.write("error 1-36\n")
	xcm_file.close()
	
