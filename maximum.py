# Colette Gallagher, 2018-04-19
# Iris Project
# To find the Maximum Value of each column of the Iris Data Set (Values in centimetres)

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

# Calculate the Maximum Value of the four columns using 'max' from the NumPy library

maxfirstcol = numpy.max(data[:,0])
maxsecondcol = numpy.max(data[:,1])
maxthirdcol = numpy.max(data[:,2])
maxfourthcol = numpy.max(data[:,3])

# Print answers

print('The maximum value of the Sepal Length is', maxfirstcol,'cm')
print('The maximum value of the Sepal Width is', maxsecondcol,'cm')
print('The maximum value of the Petal Length is', maxthirdcol,'cm')
print('The maximum value of the Petal Width is', maxfourthcol,'cm')

# Answers - The Maximum Value of the Columns in the Iris Dataset
# The maximum value of the Sepal Length is 7.9 cm
# The maximum value of the Sepal Width is 4.4 cm
# The maximum value of the Petal Length is 6.9 cm
# The maximum value of the Petal Width is 2.5 cm
