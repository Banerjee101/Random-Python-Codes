import numpy as np


pst = 1450.76
phab = 472
dof = 465

outp = pst + ((phab-dof)*np.log(phab))

print outp


# ~ 758 compt pulse 1 na
# ~ 763 band pulse 1 na

# ~ 1606 compt pulse 2
# ~ 1493 band pulse 2
