#Old Geyser 
#Brian Condon 9/4/18 Data Analysis Practice

#Calculate the mean of each column
import numpy

#Read data file into array
data = numpy.genfromtxt('data/oldgeyser.csv', delimiter=',')

firstcol = data[:,0]
meanfirstcol = numpy.mean(data[:,0])

print("Average of first column is",meanfirstcol)

import matplotlib.pyplot as pl
pl.hist(firstcol)
pl.show()