import numpy as np
 
# format a(b,c)
a = -5.19434
b = -5.20126
c = -5.18647

val = (10**a)
ll = (10**b) - val
ul = (10**c) - val

print str(val)+"_{"+str(ll)+"}^{"+str(ul)+"}"
