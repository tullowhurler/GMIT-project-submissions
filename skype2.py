#Solution 2 
#16/3/18 Ian's Solution

def ispalindrome(s): # s is the string
  ans = True 
  
  for i in range(len(s)):
      if s[i] != s[len(s) - 1 -i]: # len s of radar is = 5 as there is 5 digits, we want to get to 0-4 so have to -1, i starts at 0 and  
          ans = False 

  return ans

print(ispalindrome("radar"))
print(ispalindrome("radars"))