#python3.7

def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n%2)
