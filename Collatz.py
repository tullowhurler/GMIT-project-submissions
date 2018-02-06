# Brian Condon 06/02/18
# Collatz Conjecture

n = 17 

while n == 17:
  if n % 2 == 0:
    n = n / 2         # if even divide by 2
    print(n)
  elif n % 2 >= 0:
    n = n * 3 + 1     # if odd multiply by 3 and add 1 
    print (n) 
    # first bit of code without the integer prompt, sequence ran 17,52,26,13,40,20,10,5,16,8,4,2,1
    
    
