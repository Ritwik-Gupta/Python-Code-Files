#python3.7

t = int(input('Enter the number:'))
flag=0

for i in range(2,int(t**(0.5))):
    if(t%i==0):
        print("Not Prime")
        flag=1
        break
    else:
        continue

if(flag==0):
    print("Prime")
    
        
