#Brian Condon
# 28/02/18 Week 5 formatting exercise

print("petal length, petal width, sepal length, sepal width") #prints the headings

with open("data/iris.csv") as data_file: #opens the data file
  
    for line in data_file:               #loops through the data file

         print('{:13} {:12} {:13} {:8}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))  #spaces the columns and prints the formatted results
        
            

