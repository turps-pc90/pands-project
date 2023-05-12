# other.py
# This script will display a selection of Seaborn data visualisation options for user. Based on the Kaggle 
# guide here - https://www.kaggle.com/code/rakesh6184/seaborn-plot-to-visualize-iris-data/notebook
# Author: Paul Callaghan
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Importing dataset and creating dataframe
df = pd.read_csv('IrisDataset.csv')

# Removing ID column from dataframe as it is not needed but all other columns will be.
# "axis=1" specifies column axis. "inplace=True" ensures original dataframe used and new one not created
df.drop('Id', axis=1, inplace=True)

# FacetGrid 
def iris_facetgrid():
    # Prompt for user to select whether facetgrid is based on sepal or petal measurement
    measurement = input("Enter the measurement to plot (sepal or petal): ")
    #.lower argument used to prevent issue with user's choice of case
    if measurement.lower() == 'sepal':
        # Plot sepal measurements. 'hue' parameter divides plots by species and assigns different colours to each species 
        sns.FacetGrid(df, hue='Species', height=5).map(plt.scatter,'SepalLengthCm', 'SepalWidthCm').add_legend()
    elif measurement.lower() == 'petal':
        # Plot petal measurements  parameter divides plots by species and assigns different colours to each species
        sns.FacetGrid(df, hue='Species', height=5).map(plt.scatter,'PetalLengthCm', 'PetalWidthCm').add_legend()
    else:
        # Handle invalid input
        print("Invalid input. Please enter either 'sepal' or 'petal'.")
    plt.show()    

# Violin Plot - User will select which measurement to base the violin plot on
def iris_violin():
    
    # Prompt for user to select which column they are basing the violin plot on
    print("Select a measurement column:")
    print("1. Sepal Length")
    print("2. Sepal Width")
    print("3. Petal Length")
    print("4. Petal Width")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        column = 'SepalLengthCm'
    elif choice == '2':
        column = 'SepalWidthCm'
    elif choice == '3':
        column = 'PetalLengthCm'
    elif choice == '4':
        column = 'PetalWidthCm'
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
        exit()
    sns.violinplot(x='Species', y=column, data=df, size=7)
    plt.show()

# Pair Plot
def iris_pairplot():
    sns.pairplot(df,hue='Species')
    plt.show()

# Uncomment lines below to test if functions working
#if __name__ == '__main__': 
    #iris_facetgrid()
    #iris_violingrid()
    #iris_pairplot()
        