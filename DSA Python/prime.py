#python3.7

p = int(input())
c=0

for i in range(2,int(p/2)+1):
    if(p%i==0):
        print("NotPrime")
        c=1
        break

if(c==0):
    print("Prime")
  
