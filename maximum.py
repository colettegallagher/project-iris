# Colette Gallagher, 19th April 2018
# Iris Project
# To find the Maximum Value of each column of the Iris Data Set

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

# Calculate the Maximum Value of the four columns

maxfirstcol = numpy.max(data[:,0])
maxsecondcol = numpy.max(data[:,1])
maxthirdcol = numpy.max(data[:,2])
maxfourthcol = numpy.max(data[:,3])

# Print answers

print('The maximum value of the Sepal Length is', maxfirstcol)
print('The maximum value of the Sepal Width is', maxsecondcol)
print('The maximum value of the Petal Length is', maxthirdcol)
print('The maximum value of the Petal Width is', maxfourthcol)

# Answers - The Maximum Value of the Columns in the Iris Dataset
# The maximum value of the Sepal Length is 7.9
# The maximum value of the Sepal Width is 4.4
# The maximum value of the Petal Length is 6.9
# The maximum value of the Petal Width is 2.5
