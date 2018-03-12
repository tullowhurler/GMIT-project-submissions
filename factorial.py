# Brian Condon
# 12/3/18
# Exercise 6, Factorials 

# code sourced from https://www.programiz.com/python-programming/examples/factorial and edited to my own requirements
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print("The factorial of" , num, "is", factorial)

num1 = 7
factorial = 1
for i in range(1, num1 + 1):
    factorial = factorial * i
print("The factorial of" , num1, "is", factorial)

num2 = 10
factorial = 1
for i in range(1, num2 + 1):
    factorial = factorial * i
print("The factorial of" , num2, "is", factorial)

# I also found an even easier solution to the problem but was not sure if this was an adequate answer as there is very little code.
import math
print("The factorial of the number 5 is", math.factorial(5))
print("The factorial of the number 7 is", math.factorial(7))
print("The factorial of the number 10 is", math.factorial(10))

# solution sourced from https://learnandlearn.com/python-programming/python-reference/how-to-find-factorial-python-using-factorial-function
