#python3.7

s = input()
a=list(s)

for i in range(int(len(a)/2)):
    t=a[i]
    a[i] = a[len(a)-i-1]
    a[len(a)-i-1] = t
        
print(''.join(a))
