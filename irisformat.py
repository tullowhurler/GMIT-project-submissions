#Brian Condon
# 28/02/18 Week 5 formatting exercise

# prints the headings
# opens the data file
print("petal length, petal width, sepal length, sepal width")
with open("data/iris.csv") as data_file: 

# loops through the data file
# prints and formats the data using the line split
    for line in data_file:              

         print('{:13} {:12} {:13} {:8}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3])) 
        
            

