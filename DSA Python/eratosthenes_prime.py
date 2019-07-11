#python 3.7
'''
while(True):
    text = input()

    n = len(text)
    count=0

    for i in range(0,int(n/2)):
        if(text[i]==text[n-i-1]):
            count+=1
        else:
            break

    if(count==int(n/2)):
        print("Palindrome")
    else:
        print("Not Palindrome")
'''

while(True):
    text = input()
    
    def isPalin(s,i,e):
        if(e-i==0):
            return("Paloindrome")
        elif(s[i]!=s[e]):
            return("Not Palindrome")
        else:
            isPalin(s,i+1,e-1)

    print(isPalin(text,0,len(text)-1))


    
