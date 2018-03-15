#15/03/18 Skype with Ian problems and solutions.
#Brian Condon
#Problem 1 Summultiply
x = 11
y = x + 11

while y < 140: #while loop works as we know the answer
    y = x + y
print(y)    #my solution, just realised it was not a function 

def summultiply(x,y):
  total = 0 
  for i in range(y):   # i doesnt matter, unuasul for loop
    total = total + x  # need to keep adding total to x 
  return total 
print(summultiply(11,13))
print(summultiply(5,123)) # Ian's solution