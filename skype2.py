#Solution 2 
#16/3/18 Ian's Solution

def ispalindrome(s): # s is the string
  ans = True # thats what will print out
  
  for i in range(len(s)): #  loops through s which we put down in print
      if s[i] != s[len(s) - 1 -i]: # len s of radar is = 5 as there is 5 digits, we want to get to 0-4 so have to -1, i starts at 0 and  
          ans = False # if i is not = i returns false

  return ans    # have to have return in the function

print(ispalindrome("eye"))
print(ispalindrome("eyes"))