#Task 4
      
#import math,sys
#for r in sys.argv[1:]:
#    try:
#        x = float(r)
#        if x > 0:
#            y = math.log(x)
#            print ( 'ln ( %f ) = %g' % (x,y) )
#        else: 
#            print ( 'ln ( %f ) is illegal' % (x) )
#    except : 
#        print ("only IaN logarifm we can calculate")

#import math,sys
#x=len(sys.argv)
#rangelist=range(1,x,1)
#for i in rangelist:
#    try:
#        x = float(sys.argv[i])
#        if x > 0:
#            y = math.log(x)
#            print ( 'ln ( %f ) = %g' % (x,y) )
#        else: 
#            print ( 'ln ( %f ) is illegal' % (x) )
#    except : 
#        print ("only IaN logarifm we can calculate")

import math,sys
z=len(sys.argv)
i=1
while i <= z:
    try:
        x = float(sys.argv[i])
        if x > 0:
            y = math.log(x)
            print ( 'ln ( %f ) = %g' % (x,y) )
        else: 
            print ( 'ln ( %f ) is illegal' % (x) )
    except: 
        print ("only IaN logarifm we can calculate")
    i=i+1
