#Brian Condon
# 28/02/18 Week 5 formatting exercise

with open("data/iris.csv") as data_file:

    for line in data_file:

        line = line.replace(',', ' ')
        line = line.rstrip()
        print(line[:11], line[12:16].strip())
      

        