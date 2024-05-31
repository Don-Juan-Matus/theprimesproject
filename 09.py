import math
import numpy as np
import time
start = time.time()
# manually enter a prime numbers list 
# starting from 2 and always add 1 to the begining
ORIGIN=[1,2,3,5,7]
TOP=ORIGIN.copy()
TOP=TOP.pop()**2
# top calc
a=ORIGIN.copy()
a=a[1:-1]
b=math.prod(a) ## top common base, int
c=[b//i for i in a]
d=a.pop()
e=[d*i for i in c]
f=a[-1]*c[-1]
e[-1]=f
e.append(TOP) ## top source, list
e.reverse()
print("Input: ",ORIGIN)
h=np.cumsum(e)
h[::-1].sort() #YRY numbers limit, np array
k=h.size #loops counter
print("YRY numbers limit: ",h)
# YRY numbers and SURE math op.
origin=np.array(ORIGIN)
origin=np.delete(origin,-1)
SUre=np.empty((0),dtype=int)
suRE=np.empty((0),dtype=int)
SURE=np.empty((0),dtype=int)
m=np.empty((0),dtype=int) # assistant array for SUre
n=np.empty((0),dtype=int) # assistant array for suRE
cycles=0
for g in range(len(origin)):
    origin=np.delete(origin,g)
    yry=[]
    for i in origin:        
        i=np.prod(origin)*i        
        yry.append(i)
    print(yry)    
    if cycles==0:
        YRY=yry
        YRY=np.array(YRY)
        limit=cycles+1
    if cycles>0:
        SUre=SUre[0:0]
        suRE=suRE[0:0]
        print("\n","Loop: ",cycles,"/",k-1)
        print("limit",limit)
        yry=np.array(yry)
        for Y in range(len(YRY)):            
            for y in range(len(yry)):                
                m=np.add(YRY[Y], yry[y])
                #print(m)
                hook1=0
                if m>0 and m<h[limit] and hook1==0:
                    SUre= np.append(SUre,m)
                    hook1+=1
                    if m not in SUre and hook1!=0:
                      SUre= np.append(SUre,m)
                      #SUre=np.unique(SUre)
        print("SU array:" ,SUre)        
        for Y in range(len(YRY)):            
            for y in range(len(yry)):                
                n=np.subtract(YRY[Y], yry[y])
                #print(n)
                hook2=0
                if n>0 and n<h[limit] and hook2==0:
                    suRE= np.append(suRE,n)
                    hook2+=1
                    if n not in suRE and hook2!=0:
                      suRE= np.append(suRE,n)
                      
                    #suRE=np.unique(suRE)
        print("RE array:" ,suRE)        
        SURE=np.concatenate((SUre,suRE))        
        SURE=np.unique(SURE)
        SURE=np.sort(SURE)
        print("SURE array:" ,SURE)
        print("SURE array size: ",SURE.size)        
        YRY=SURE
        limit+=1
    limit=cycles+1
    origin=ORIGIN[:-1]    
    cycles+=1    
print("\n","PRIMES: ",YRY)
end = time.time()
print("time in seg: ",end-start)
