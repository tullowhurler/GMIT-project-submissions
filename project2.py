# Brian Condon
# Even Fibonacci numbers
# answer from https://stackoverflow.com/questions/23168502/sum-of-even-fibonacci-numbers-below-4-million-python

a, b = 1, 1
total = 0
while a <= 4000000:
    if a % 2 == 0:
        total += a # adds onto whatever a values was t=0,t+=a, t=0+a
    a, b = b, a+b  # the real formula for Fibonacci sequence
print(total)             

    
    