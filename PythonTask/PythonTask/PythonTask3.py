#Task 3

import sys , random
def compute (n):
    i = s = 0
    while (i <= n):
        s += random . random ()
        i += 1
    return s / n
n = int(sys . argv [1], 10)
print ('average of %d random numbers is %g ' % (n, compute(n)))