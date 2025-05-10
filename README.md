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
  
10. Visualisation of the distribution of the features (sepal length, sepal width, petal length and petal width)
Exploring the relationships and correlations between different features ussing scatter plots, regression lines plotting, heatmaps and boxplots.

**Dependencies**
numpy as np 
matplotlib.pyplot as plt
csv

**Analysis and analysis.py program structure**
1. Outputs a summary of each variable to a single text file, 
The dataset has 5 columns which represent  sepal length, sepal width, petal length, petal width and species' names.
Program uses list of features names (float type): sepal length, sepal width, petal length, petal width and species as names of the columns respectively using append and covert the list to NumPy arrays in order to calculate statistics: means, mins, maxs, standard deviation (stds), medians, also to count number of rows of features are of each species. Program creates text file called feature_output.txt with the summary of the dataset's features.

2. Saves a histogram of each variable to png files. 
For each of variables (sepal length, sepal width, petal length, and petal width), program creates a histogram using matplotlib.pyplot.hist()
Program uses matplotlib.pyplot.savefig() to save histogram of each variable.

 **Sepal Length:** The histogram for sepal length looks like a normal curve which is centred around 5.8cm, the shortest sepal is 4.3cm, the longest is 7.9cm. The spread of the sepal length iis moderate, with the standard deviation of 0.8cm. 
 
**Sepal Width** For sepal width (cm) the means is 3.0 with the minimum is 2.0, the maximum is 4.4, the standard deviation is 0.43, and the median of 3.0. It suggests a balanced spread data with one main peak, which means that there is a typical range of width that most of flowers fall into.  It indicates that this feature is not the best way to differentiate the species. 

**Petal length** For petal length (cm) the means is 3.75 with the minimum is 1.0, the maximum is 6.9, the standard deviation is 1.7, and the median of 4.35. This indicates a wider spread in petal lengths. It has 2 peaks which indicates that 2 of the 3 species have much different petal lengths.

**Petal width** For petal width (cm)the mean is 1.19 with the minimum is 0.1, the maximum is 2.5, the standard deviation is 0.7, and the median of 1.3. It has 3 peaks which can suggest that the 3 of the species significantly differ in petal width. 

4. Outputs a scatter plot of each pair of variables. 
Scatter plots visualise correlation between different variables.

**Petal length and Petal width** - the scatter plot shows positive correlation which means when petal length increases, petal width also tend to increase. We can see clear separation of the species, especialy Setosa ( in the left-botom corner) is very well separated from the other 2 species. Small amount of Versicolor's and Virginica's data point overlap.

**Sepal length and Petal length** - the scatter plot shows generally positive correlation, when sepal length increases, petal length also tend to increase.  The separation of the species is much less distinct compared to petal length and petal width, the bottom part of the plot shows Setosa to be more separated from the other two species. Virginica has a longer spread that the other two scpecies.

**Sepal length and Petal width** - the scatter plot shows less correlation between these two, with majority of the data point overlapping. Setosa has smallest range of both features. Versicolor and Virginica are significantly overlapping, which makes them difficult to distinguish based only on these two features.  

**Sepal width and Petal length** - the scatter plot shows a weak positive correlation, Setosa tends to have smaller petal lengths and a moderate range of sepal widths, showing some separation from the other two species. Versicolor's and Virginica's data points are significantly overlapping, which makes them difficult to distinguish based only on these two features.  Virginica has the longest petal length and sepak width.

**Sepal width and Petal width** - the scatter plot shows a weak correlation, with most of the data points overlapping. 

5. Regression line for Petal length nad petal width to visualise the positive correlation between these two features.

**Acknowledgement**

https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/

https://www.analyticsvidhya.com/blog/2022/06/iris-flowers-classification-using-machine-learning/

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html

https://www.w3schools.com/python/ref_func_enumerate.asp

https://www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib/

https://en.wikipedia.org/wiki/Simple_linear_regression#Line_fitting

https://www.geeksforgeeks.org/right-skewed-histogram/#what-is-a-histogram

http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html#:~:text=5.8%202.2%20virginica-,Exploratory%20Data%20Analysis,classes%20%2D%2D%20is%20that%20true%3F
