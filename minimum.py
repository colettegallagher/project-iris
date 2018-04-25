# Colette Gallagher, 2018-04-19
# Iris Project
# To find the Minimum Value of each column of the Iris Data Set (values measured in centimetres)

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

# Calculate the Minimum Value of the four columns using 'min' from the NumPy library

minfirstcol=numpy.min(data[:,0])
minsecondcol=numpy.min(data[:,1])
minthirdcol=numpy.min(data[:,2])
minfourthcol=numpy.min(data[:,3])

# Print answers

print('The minimum value of the Sepal Length is', minfirstcol,'cm')
print('The minimum value of the Sepal Width is', minsecondcol,'cm')
print('The minimum value of the Petal Length is' minthirdcol,'cm')
print('The minimum value of the Petal Width is', minfourthcol,'cm')

# Answers - The Minimum Value of the Columns in the Iris Dataset:
# The minimum value of the Sepal Length is 4.3 cm
# The minimum value of the Sepal Width is 2.0 cm
# The minimum value of the Petal Length is 1.0 cm
# The minimum value of the Petal Width is 0.1 cm
