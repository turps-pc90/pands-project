# scatterplot.py
# This file will present the scatterplots for the variables relating to Fisher-Iris Dataset - based on the guide to create Python menus on this URL - https://matplotlib.org/stable/gallery/shapes_and_collections/scatter.html#sphx-glr-gallery-shapes-and-collections-scatter-py
# The focus will be on displaying the relationship between the width and length of sepals and petals of each of the three types of Iris

# Author: Paul Callaghan

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('IrisDataset.csv')

# Creating variables for the three species (based on article here - https://www.geeksforgeeks.org/difference-between-loc-and-iloc-in-pandas-dataframe/)
setosa = df.loc[df['species'] == 'Iris-setosa']
versicolor = df.loc[df['species'] == 'Iris-versicolor']
virginica = df.loc[df['species'] == 'Iris-virginica']



