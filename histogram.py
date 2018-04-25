# Colette Gallagher, 2018-04-19
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

# Imports the matplotlib library to create a histogram and call it pl

import matplotlib.pyplot as pl

# Prints the data for Sepal Length as a histogram

pl.hist(firstcol)
pl.show()

# Prints the data for Sepal Width as a histogram

pl.hist(secondcol)
pl.show()

# Prints the data for Petal Length as a histogram

pl.hist(thirdcol)
pl.show()

# Prints the data for Petal Width as a histogram

pl.hist(fourthcol)
pl.show()

# Histograms are then saved as jpeg files on the PC and imported into Github using the UPLOAD FILES button 
# which is found on the top right of the screen above the contents list of the repository

