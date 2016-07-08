import sys , math
try :
    infilename = sys . argv [1]
    outfilename = sys . argv [2]
except :
    print (" Usage:" , sys.argv [0] , " infile outfile ")
    sys . exit (1)
ifile = open (infilename , 'r')
ofile = open (outfilename , 'w')

def myfunc (y):
    if y >= 0.0:
        return y**5*math.exp(- y)
    else :
        return 0.0

for line in ifile :
    M = line.split()
    n=len(M)
    sum=0
    for m in M:
        m=float(m)
        ofile . write ('%12.6f \t' %(m))
        sum=sum+m
    ofile.write('%12.6f \n' %(sum/n))
ifile . close ()
ofile . close ()