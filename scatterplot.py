# scatterplot.py
# This file will present the scatterplots for the variables relating to Fisher-Iris Dataset - based on the guide to create 
# scatterplots on this URL - https://matplotlib.org/stable/gallery/shapes_and_collections/scatter.html#sphx-glr-gallery-shapes-and-collections-scatter-py
# The focus will be on displaying the relationship between the width and length of sepals and petals of each of the three types of Iris
# Author: Paul Callaghan

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('IrisDataset.csv')

# Creating variables for the three species (based on article here - https://www.geeksforgeeks.org/difference-between-loc-and-iloc-in-pandas-dataframe/)
setosa = df.loc[df['Species'] == 'Iris-setosa']
versicolor = df.loc[df['Species'] == 'Iris-versicolor']
virginica = df.loc[df['Species'] == 'Iris-virginica']

# Creating variables for each of the measurements within dataset
# Setosa measurements
setosa_petw = setosa['PetalWidthCm']
setosa_petl = setosa['PetalLengthCm']
setosa_sepw = setosa['SepalWidthCm']
setosa_sepl = setosa['SepalLengthCm']

# Versicolor measurements
versicolor_petw = versicolor['PetalWidthCm']
versicolor_petl = versicolor['PetalLengthCm']
versicolor_sepw = versicolor['SepalWidthCm']
versicolor_sepl = versicolor['SepalLengthCm']

# Virginica measurements
virginica_petw = virginica['PetalWidthCm']
virginica_petl = virginica['PetalLengthCm']
virginica_sepw = virginica['SepalWidthCm']
virginica_sepl = virginica['SepalLengthCm']

# Create Petal Scatterplot
def scatterplot_petals():
    # Setosa Plot Points
    plt.scatter(setosa_petl, setosa_petw, label='Setosa', color='purple')
    # Versicolor Plot Points
    plt.scatter(versicolor_petl, versicolor_petw, label='Versicolor', color='darkgreen')
    # Virginica Plot Points
    plt.scatter(virginica_petl, virginica_petw, label='Virginica', color='brown')
    plt.xlabel('Petal Length(Cm)')
    plt.ylabel('Petal Width(Cm)')
    plt.legend()
    plt.show()

# Create Sepal Scatterplot
def scatterplot_sepals():
    # Setosa Plot Points
    plt.scatter(setosa_sepl, setosa_sepw, label='Setosa', color='purple')
    # Versicolor Plot Points
    plt.scatter(versicolor_sepl, versicolor_sepw, label='Versicolor', color='darkgreen')
    # Virginica Plot Points
    plt.scatter(virginica_sepl, virginica_sepw, label='Virginica', color='brown')
    plt.xlabel('Sepal Length(Cm)')
    plt.ylabel('Sepal Width(Cm)')
    plt.legend()
    plt.show()
