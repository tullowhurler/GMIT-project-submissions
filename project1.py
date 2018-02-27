# Brian Condon Project Eulor Part 1
#If we list all the natural numbers below 10 
# that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
# Ian's solution 

sum = 0
i= 1

while i < 1000:
	if i % 3 == 0:
	 sum = sum + i # makes sense, thats how it adds i, have to keep adding it up
	elif i % 5 == 0:
	 sum = sum + i
	i = i + 1 # have to change i by 1 to continue the loop
print (" sum of multiples of 3 + 5, less than a 1000:", sum)  

# github