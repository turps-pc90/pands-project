# Programming & Scripting Project

## Author: Paul Callaghan

### Project Name:

Iris Dataset Analysis

### Project Description:

This project is intended to present the Fisher Iris dataset in a meaningful manner by utilising the Python programming language to create at least a histogram, a scatterplot and a summary text file (with possibly more to be added).

#### Table of Contents

- [Initial Research](#initial-research)
- [Creating User Menu](#creating-user-menu)
- [Usage](#usage)
- [Findings](#findings)
- [References](#references)

#### Initial Research<a id="initial-research"></a>

Based on Chapter 3 (section 2) of 'Mark Fenner's Machine Learning with Python for Everyone', the dataset is named after Sir Ronald Fisher, a statistician from the mid-20th century however it was in fact Edgar Anderson that gathered the data.

The dataset was downloaded from Kaggle (Retrieved 08/04/2023, from https://www.kaggle.com/datasets/uciml/iris?resource=download). 

In the dataset, there are four measurements per iris - sepal length, sepal width, petal length and petal width (all in centimetres). The sample size of data for each species is 50 based on there being 50 rows of data for each of the species.

![alt text](https://www.google.com/url?sa=i&url=https%3A%2F%2Fgithub.com%2Fsimonava5%2Ffishers-iris-data&psig=AOvVaw1qmFwvDM_6B5-hPLybYKMF&ust=1682621508963000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCJjg492byP4CFQAAAAAdAAAAABAE)

The three types of iris are the Iris Setosa, Iris Versicolor and the Iris Virginica.

#### Creating User Menu<a id="creating-user-menu"></a>

The analysis.py script contains the menu where the user can select from 4 functions or to exit the application.

1: 'Output Summary Of Each Variable'

Option 1: The first option in analysis.py is to call the summary_output function which is imported from summary.py. Using Pandas, the IrisDataset.csv is read into a dataframe and grouped by the species type - iris setosa, iris versicolor and iris virginica. 'time' is imported to created a timestamp for unique filenames so user can see when file is written within the name.

A loop is created with variables to output a unique sentence for each of the species types. F-Strings are used for outputting the variables into the text file.

2: 'Save Histogram Of Each Variable'

The histogram.py is imported and contains three functions. Any of these functions can be run when the user selects option 2 from the menu. The functions are based on the plottask.py task from a few weeks ago. Copied functions from summary.py to calculate averages of petal and sepal measurements for each of three iris species.

The sub menu initially caused difficulties when trying to import it as it's own function from histogram.py so I moved the function to the analysis.py file and works after testing. 

3: 'Output Scatter Plot Of Each Pair Of Variables'

4: 'To Be Decided'

5: 'Exit'

#### Usage<a id="usage"></a>

Explanation for how to use the project

#### Findings<a id="findings"></a>

To be completed.

#### References<a id="references"></a>

UCI Machine Learning Repository. (n.d.). Iris Data Set. Kaggle. Retrieved 08/04/2023, from https://www.kaggle.com/datasets/uciml/iris?resource=download.

Nemec, A. (2018, December 5). How to write a good README file. freeCodeCamp. Retrieved 08/04/2023, from https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/.

Fenner, M. (2019). Machine Learning with Python for Everyone. Pearson.

Matsiko, F. (2019, June 25). How to Create a Menu for a Python Console Application. Computing Learner. Retrieved April 23, 2023, from https://computinglearner.com/how-to-create-a-menu-for-a-python-console-application/.

Stack Exchange Inc. (2012, May 16). How to create a file name with the current date & time in Python?. Stack Overflow. Retrieved April 23, 2023, from https://stackoverflow.com/questions/10607688/how-to-create-a-file-name-with-the-current-date-time-in-python.

Liu, D. (2021, August 12). Reading and Writing CSV Files in Python. Real Python. Retrieved April 23, 2023, from https://realpython.com/python-csv/.

Pandas GroupBy: Your Guide to Grouping Data in Python. Real Python. URL: https://realpython.com/pandas-groupby/#the-hello-world-of-pandas-groupby (accessed April 22, 2023)

Pandas GroupBy - One Column and Get Mean, Min, and Max values. GeeksforGeeks. URL: https://www.geeksforgeeks.org/pandas-groupby-one-column-and-get-mean-min-and-max-values/ (accessed April 22, 2023)

Schafer, C. (2019, January 7). Matplotlib Tutorial (Part 6): Histograms [Video]. YouTube. https://www.youtube.com/watch?v=XDv6T4a0RNc&t=306s

Matplotlib Development Team. (2021). matplotlib.axes.Axes.hist. Matplotlib 3.4.2 documentation. Retrieved September 27, 2021, from https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html

#### Packages Used In Project

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) - https://www.python.org/downloads/

![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) - https://pandas.pydata.org/ - "is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language."

![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) - https://matplotlib.org/ - "Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python."

![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) - https://numpy.org/ - "The fundamental package for scientific computing with Python"
