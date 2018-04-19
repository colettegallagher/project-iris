# Colette Gallagher, 19th April 2018
# Iris Project
# To find the Minimum Value of each column of the Iris Data Set

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

# Calculate the Minimum Value of the four columns

minfirstcol=numpy.min(data[:,0])
minsecondcol=numpy.min(data[:,1])
minthirdcol=numpy.min(data[:,2])
minfourthcol=numpy.min(data[:,3])

# Print answers

print('The minimum value of the Sepal Length is', minfirstcol)
print('The minimum value of the Sepal Width is', minsecondcol)
print('The minimum value of the Petal Length is' minthirdcol)
print('The minimum value of the Petal Width is', minfourthcol)

# Answers - The Minimum Value of the Columns in the Iris Dataset
# The minimum value of the Sepal Length is 4.3
# The minimum value of the Sepal Width is 2.0
# The minimum value of the Petal Length is 1.0
# The minimum value of the Petal Width is 0.1
