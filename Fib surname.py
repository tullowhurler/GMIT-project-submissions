# Brian Condon Week 1
# A program that displays Fibonacci numbers.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 16
ans = fib(x)
print("Fibonacci number", x, "is", ans)

# My name is Brian, so the first and last letters of my name ( B+N= 2+14) equal 16. The 16th fibonacci number is 987.

# Week 2 exercise Brian Condon
# A program that displays Fibonacci numbers using people's names.

def fib(n):

  """This function returns the nth Fibonacci number."""

  i = 0

  j = 1

  n = n - 1

 while n >= 0:

    i, j = j, i + j

    n = n - 1

  

  return i

name = "Condon"

first = name[0]

last = name[-1]

firstno = ord(first)

lastno = ord(last)

x = firstno + lastno

ans = fib(x)

print("My surname is", name)

print("The first letter", first, "is number", firstno)

print("The last letter", last, "is number", lastno)

print("Fibonacci number", x, "is", ans)

# My surname is Condon. The first letter C is number 67 The last letter n is number 110
# Fibonacci number 177 is 4378519841510949178490918731459856482
# I got the definition for the Ord function from hovering over it on the Visual Studio, it said that it would return the Unicode point for a one-code string.
# I did not quite understand the definition so kept digging and found  that ord() short form of 'ordinal' which means a number defining the position of something in a series, such as first , ˜second, or ˜third. 
# This function is useful for converting a single character to its corresponding ASCII value so C = 67, n =110 etc.
