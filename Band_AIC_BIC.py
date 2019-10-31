import numpy as np

pha_bins = 678
dof = 674
pgstat = input("Enter PG stat :")



AIC = 2*(pha_bins - dof) + pgstat
BIC = pgstat + (pha_bins - dof)*np.log(pha_bins)

print "\nThe AIC is :"+str(AIC)+"\n"
print "The BIC is :"+str(BIC)+"\n"
