#Вероятность 5% играть не стоит
import sys,random
n=float(sys.argv[1])
i=1
k=0
while i<=n:
    x=random.randint(1,6)
    y=random.randint(1,6)
    z=random.randint(1,6)
    w=random.randint(1,6)
    if ((x+y+z+w)<9):
        k=k+1
    i=i+1
print("Probability of win= %f" %(k/n))