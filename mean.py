# Colette Gallagher, 19th April 2018
# Iris Project
# To find the mean of each column of the Iris Data Set (values are measured in centimetres)

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

# Calculate the mean of the four columns

meanfirstcol=numpy.mean(data[:,0])
meansecondcol=numpy.mean(data[:,1])
meanthirdcol=numpy.mean(data[:,2])
meanfourthcol=numpy.mean(data[:,3])

# Print answers

print('The mean of the Sepal Length is', meanfirstcol,'cm')
print('The mean of the Sepal Width is', meansecondcol,'cm')
print('The mean of the Petal Length is' meanthirdcol,'cm')
print('The mean of the Petal Width is', meanfourthcol,'cm')

# Answers - The Mean of the Columns in the Iris Dataset
# The mean of the Sepal Length is 5.84 cm
# The mean of the Sepal Width is 3.054 cm
# The mean of the Petal Length is 3.76 cm
# The mean of the Petal Width is 1.20 cm
