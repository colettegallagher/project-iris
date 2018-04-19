# Colette Gallagher, 19th April 2018
# Iris Project
# To find the Median of each column of the Iris Data Set

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

# Calculate the Standard Deviation Value (SD)of the four columns (measured in centimeters)

medianfirstcol = numpy.median(data[:,0])
mediansecondcol = numpy.median(data[:,1])
medianthirdcol = numpy.median(data[:,2])
medianfourthcol = numpy.median(data[:,3])

# Print answers

print('The Median value of the Sepal Length is', medianfirstcol,'cm')
print('The Median value of the Sepal Width is', mediansecondcol,'cm')
print('The Median value of the Petal Length is', medianthirdcol,'cm')
print('The Median value of the Petal Width is', medianfourthcol,'cm')

# Answers - The Median Values of the four columns of the Iris Data Set
The Median value of the Sepal Length is 5.8 cmThe Median value of the Sepal Width is 3.0 cm
The Median value of the Petal Length is 4.35 cm
The Median value of the Petal Width is 1.3 cm
