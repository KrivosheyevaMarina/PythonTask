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