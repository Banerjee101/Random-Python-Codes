import os



def make_phas(obs, det):
	for row in range(0,21):
		cmppha_cmd = 'cmppha infile='+obs+'_'+det+'_srcspectra_v01.pha outfile='+det+'_src'+str(row+1)+'.pha cmpmode=expand rows='+'\"'+str(row+1)+'\"'
		cmppha_cmd_bak = 'cmppha infile='+obs+'_'+det+'_bkgspectra.bak outfile='+det+'_bak'+str(row+1)+'.bak cmpmode=expand rows='+'\"'+str(row+1)+'\"'
		# ~ cmppha_cmd_rsp = 'cmppha infile='+obs+'_'+det+'_weightedrsp.rsp outfile='+det+'_weightedrsp'+str(row+1)+'.rsp cmpmode=expand rows='+'\"'+str(row+1)+'\"'
		print(cmppha_cmd)
		print(cmppha_cmd_bak)
		# ~ print(cmppha_cmd_rsp)
		print("Making pha I for ", row, " ",  cmppha_cmd)
		os.system(cmppha_cmd)
		os.system(cmppha_cmd_bak)
		# ~ os.system(cmppha_cmd_rsp)
		
		
obs_id = 'bn190829830'

		
make_phas(obs_id, 'n6')
make_phas(obs_id, 'n7')
# ~ make_phas(obs_id, 'b0')
make_phas(obs_id, 'b1')
# ~ make_phas(obs_id, 'n7')
# ~ make_phas(obs_id, 'n8')
