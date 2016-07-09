#Аналитиеское решение:11/36~0.3055555
#из теории больших чисел выходит, что нам необходимо 1000000 испытаний,
#по факту достаточно 200000 экспериментов

import sys,random
n=float(sys.argv[1])
i=1
k=0
while i<=n:
    x=random.randint(1,6)
    y=random.randint(1,6)
    if (x==6 or y==6):
        k=k+1
    i=i+1
print("Probability= %f" %(k/n))