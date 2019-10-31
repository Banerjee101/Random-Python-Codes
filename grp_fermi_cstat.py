import os






for i in range(0,10):
    grp_cmd = """echo \""""+"""glg_tte_b1_bn171010792_v0"""+str(i)+""".pha1\n""" \
    """!"""+"""glg_tte_b1_bn171010792_v"""+str(i)+"""_pgstat.pha1\n"""\
    + """chkey RESPFILE """+"""glg_cspec_b1_bn171010792_v02.rsp2{3}\n""" \
    + """chkey BACKFILE """+"""glg_tte_b1_bn171010792_v0"""+str(i)+""".bak\n""" \
    +"""exit\n\" | grppha"""
    print grp_cmd
    os.system(grp_cmd)

