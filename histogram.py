# Colette Gallagher, 19th April 2018
# project - iris
# Data set analysis using histogram

# Run ipython program in python

ipython

# Import NumPy library

import numpy

# Read Iris data file into array

data = numpy.genfromtxt('data/iris.csv',delimiter = ',')

# Specify the columns of data to be read

firstcol = data[:,0]
secondcol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:,3]

# Imports the matplotlib library to create a histogram

import matplotlib.pyplot as pl

# Prints the data for Sepal Length as a list and then as a histogram

pl.hist(firstcol)
pl.show()

# Prints the data for Sepal Width as a list and then as a histogram

pl.hist(secondcol)
pl.show()

# Prints the data for Petal Length as a list and then as a histogram

pl.hist(thirdcol)
pl.show()

# Prints the data for Petal Width as a list and then as a histogram

pl.hist(fourthcol)
pl.show()
