#Task 4
      
import math,sys
for r in sys.argv[1:]:
    try:
        x = float(r)
        if x > 0:
            y = math.log(x)
            print ( 'ln ( %f ) = %g' % (x,y) )
        else: 
            print ( 'ln ( %f ) is illegal' % (x) )
    except : 
        print ("only IaN logarifm we can calculate")