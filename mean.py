# Colette Gallagher, 19th April 2018
# Project - Iris
# To find the mean of each column of the Iris Data Set

# Run ipython program in python

ipython

# Import NumPy library

import numpy

# Read Iris data file into array

data = numpy.genfromtxt('data/iris.csv',delimiter = ',')

# Specify the column of data to be read

firstcol = data[:,0]

# Calculate the mean of the first column

meanfirstcol=numpy.mean(data[:,0])

# Print answer

meanfirstcol

# The mean of the first column is 5.8433
