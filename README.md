PROGRAMMING AND SCRIPTING Project
by Justyna Pinkowska 

**Technologies:**
Python
Git
GitHub

**Dataset:**

**Name:** Iris Dataset

**Source:** https://archive.ics.uci.edu/dataset/53/iris

**Description:** 
The Iris dataset contains measurements for 150 Iris flowers from three different species: Setosa, Versicolor, and Virginica. The dataset includes four features: petal length, petal width, sepal length and sepal width.

**Project structure**
1. analysis.py This is a program that contains the Python code used to perform the analysis.
Loading and inspecting the Iris dataset from a file iris.csv, in order to do so I imported "csv" library Comma-Separated Value.
2. feature_output.txt - outputs a summary of each variable
3. README.md
4. sepal_length_histogram.png
5. sepal_width_histogram.png
6. petal_length_histogram.png
7. petal_width_histogram.png
8. .gitgnore
  
10. Visualisation of the distribution of the features (sepal lenght, sepal width, petal lenght and petal width)
Exploring the relationships and correlations between different features ussing scatter plots, regression lines plotting, heatmaps and boxplots.

**Dependencies**
numpy as np 
matplotlib.pyplot as plt
csv

**Analysis and analysis.py program structure**
1. Outputs a summary of each variable to a single text file, 
The dataset has 5 columns which represent  sepal lenght, sepal width, petal lenght, petal width and species' names.
Program uses list of features names (float type): sepal lenght, sepal width, petal lenght, petal width and species as names of the columns respectively using append and covert the list to NumPy arrays in order to calculate statistics: means, mins, maxs, standard deviation (stds), medians, also to count number of rows of features are of each species. Program creates text file called feature_output.txt with the summary of the dataset's features.

2. Saves a histogram of each variable to png files. 
For each of variables (sepal length, sepal width, petal length, and petal width), program creates a histogram using matplotlib.pyplot.hist()
Program uses matplotlib.pyplot.savefig() to save histogram of each variable.

3. Outputs a scatter plot of each pair of variables. 
 


**Acknowledgement**

https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
https://www.analyticsvidhya.com/blog/2022/06/iris-flowers-classification-using-machine-learning/
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
https://www.w3schools.com/python/ref_func_enumerate.asp
https://www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib/


