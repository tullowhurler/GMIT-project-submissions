# Ian's function code for adding up
def sumall(upto): 
    sumupto = 0
    for i in range(1, upto + 1): 
        sumupto= sumupto + i 
    return sumupto
print("The sum of values from 1 to 50 is", sumall(50))
print("The sum of values from 1 to 5 is", sumall(5))
print("The sum of values from 1 to 10 is", sumall(10))

#Eucalidain https://app.codility.com/programmers/lessons/12-euclidean_algorithm/
def gcd(x, y):
    while x != 0 and y != 0:
        if x > y: 
            x = x % y
        else:
         y = y % x
    if x == 0:      
     return y
    else: 
     return x 
print("GCD of 6 and 15 is", gcd(6, 15))