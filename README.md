# project-iris
Project Researching Fisher's Irish Data Set

## Introduction
This project analyses Fisher's Iris Data Set using different statistical methods.

## Contents
1. History of Fisher's Iris Flower Data Set
2. Statistics Used
3. Conclusions
4. References

### 1. History
Sir Ronald Aylmer Fisher (1890-1962) was a British statistican and geneticist.

![A picture of Ronald Fisher](fisher.jpg)

Fisher introduced the Iris Flower Data Set in his 1936 paper.  The data set consists of three species of Iris:
1. Iris Setosa
2. Iris Virginica
3. Iris Versicolor

![Photo of the Iris in the data set](Iris.jpg)

Fifty samples of each of the three species were measured.  Each of the 150 samples were measured, in centimetres, and recorded in five categories:
1. Length of the Sepals
2. Width of the Sepals
3. Length of the Petals
4. Width of the Petals
5. Class

Fisher was able to develop a linear discriminant model to distinguish each of the iris species from each other.

![Principle Component Analysis of Iris data set](scatterplot.jpg)


### 2. Statistics Used
Min  Max   Mean    SD   Class Correlation
Class Distribution: 33.3% for each of 3 classes.

SD: To calculate the standard deviation of those numbers:
Work out the Mean (the simple average of the numbers)
Then for each number: subtract the Mean and square the result.
Then work out the mean of those squared differences.
Take the square root of that and we are done!

Class Correlation (https://stats.stackexchange.com/questions/57776/what-is-class-correlation)

### 3. Conclusions


### 4. References
https://en.wikipedia.org/wiki/Ronald_Fisher
http://slideplayer.com/slide/4414578/
http://web.as.uky.edu/statistics/users/pbreheny/764-f11/notes/9-20.pdf
http://scikit-learn.org/stable/_images/sphx_glr_plot_pca_vs_lda_001.png
http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names
http://archive.ics.uci.edu/ml/machine-learning-databases/iris/
http://www.learningaboutelectronics.com/Articles/How-to-compute-the-standard-deviation-in-Python-using-numpy.php
https://docs.scipy.org/doc/numpy/reference/generated/numpy.corrcoef.html

