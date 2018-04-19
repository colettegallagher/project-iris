# Colette Gallagher, 19th April 2018
# Iris Project
# To find the Standard Deviation of each column of the Iris Data Set

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

# Calculate the Standard Deviation Value (SD) of the four columns (measured in centimeters)

stdfirstcol = numpy.std(data[:,0])
stdsecondcol = numpy.std(data[:,1])
stdthirdcol = numpy.std(data[:,2])
stdfourthcol = numpy.std(data[:,3])

# Print answers

print('The standard deviation value of the Sepal Length is', stdfirstcol,'cm')
print('The standard deviation value of the Sepal Width is', stdsecondcol,'cm')
print('The standard deviation value of the Petal Length is', stdthirdcol,'cm')
print('The standard deviation value of the Petal Width is', stdfourthcol,'cm')')

# Answers - The Standard Deviation Value of the Columns in the Iris Dataset

# The standard deviation value of the Sepal Length is 0.83cm
# The standard deviation value of the Sepal Width is 0.43cm
# The standard deviation value of the Petal Length is 1.76cm
# The standard deviation value of the Petal Width is 0.76cm
