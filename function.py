def sumall(upto): 
    sumupto = 0
    for i in range(1, upto + 1): 
        sumupto= sumupto + i 
    return sumupto
print("The sum of values from 1 to 50 is", sumall(50))
print("The sum of values from 1 to 5 is", sumall(5))
print("The sum of values from 1 to 10 is", sumall(10))

