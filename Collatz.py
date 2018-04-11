# Brian Condon 06/02/18
# Collatz Conjecture without integer prompt

n = 17 
# Creating a while loop for when the n is equal to 17
while n == 17:
# If the remainder is 0 means it is an even number
  if n % 2 == 0:
# if even divide by 2
    n = n / 2         
    print(n)
# if the remainder is not 0 then the number is odd
  elif n % 2 >= 0:
# if odd multiply by 3 and add 1
    n = n * 3 + 1      
    print (n) 
# first bit of code without the integer prompt, sequence ran 17,52,26,13,40,20,10,5,16,8,4,2,1
    
# Part 2 with integer prompt 
# Brian Condon 06/02/18
# Collatz Conjecture

# code on integer prompt from http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html 
n =  int(input("enter an integer:")) 

while n!= 1:
  if n % 2 == 0:
    n = n / 2  
    print(n)
  elif n % 2 >= 0:
    n = n * 3 + 1
    print (n) 
    
    C:\Users\Tullowhurler\Desktop\Programming and Scripting\Training> python collatz.py
enter an integer: 22
11.0
34.0
17.0
52.0
26.0
13.0
40.0
20.0
10.0
5.0
16.0
8.0
4.0
2.0
1.0
    
