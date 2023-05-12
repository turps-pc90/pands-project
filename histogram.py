# histogram.py
# This function creates a histogram of each variable and basing the function on the plottask.py task
# Copied functions from summary.py to calculate averages of petal and sepal measurements for each of three iris species - 
# iris-setosa, iris-virginica and iris-versicolor
# Author: Paul Callaghan

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('IrisDataset.csv')

# Defining function to show Iris Setosa
def plot_setosa():
    # Selecting data for Iris Setosa species
    setosa_df = df[df['Species'] == 'Iris-setosa']

    # Creating subplots for each measurement, 2 rows and 2 columns with figsize of 8 x 8 inches
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8,8))

    # Creating histogram for sepal width, sepal length, petal width and petal length
    # Sepal Width Measurements (Coloured green)
    axes[0,0].hist(setosa_df['SepalWidthCm'], bins=20, color='g')
    axes[0,0].set_title('Sepal Width')

    # Sepal Length Measurements (Coloured red)
    axes[0,1].hist(setosa_df['SepalLengthCm'], bins=20, color='r')
    axes[0,1].set_title('Sepal Length')

    # Petal Width Measurements (Coloured magenta)
    axes[1,0].hist(setosa_df['PetalWidthCm'], bins=20, color='m')
    axes[1,0].set_title('Petal Width')

    # Petal Length Measurements (Coloured cyan)
    axes[1,1].hist(setosa_df['PetalLengthCm'], bins=20, color='c')
    axes[1,1].set_title('Petal Length')

    # Add a title to the plot
    plt.suptitle('Distribution of Iris Setosa Measurements')
    
    # Display the plot
    plt.show()

def plot_versicolor():
    # Selecting data for Iris Versicolor species
    versi_df = df[df['Species'] == 'Iris-versicolor']

    # Creating subplots for each measurement, 2 rows and 2 columns with figsize of 8 x 8 inches
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8,8))

    # Creating histogram for sepal width, sepal length, petal width and petal length
    # Sepal Width Measurements (Coloured green)
    axes[0,0].hist(versi_df['SepalWidthCm'], bins=20, color='g')
    axes[0,0].set_title('Sepal Width')

    # Sepal Length Measurements (Coloured red)
    axes[0,1].hist(versi_df['SepalLengthCm'], bins=20, color='r')
    axes[0,1].set_title('Sepal Length')

    # Petal Width Measurements (Coloured magenta)
    axes[1,0].hist(versi_df['PetalWidthCm'], bins=20, color='m')
    axes[1,0].set_title('Petal Width')

    # Petal Length Measurements (Coloured cyan)
    axes[1,1].hist(versi_df['PetalLengthCm'], bins=20, color='c')
    axes[1,1].set_title('Petal Length')

    # Add a title to the plot
    plt.suptitle('Distribution of Iris Versicolor Measurements')
    
    # Display the plot
    plt.show()


def plot_virginica():
    # Selecting data for Iris Virginica species
    virginica_df = df[df['Species'] == 'Iris-virginica']

    # Creating subplots for each measurement, 2 rows and 2 columns with figsize of 8 x 8 inches
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8,8))

    # Creating histogram for sepal width, sepal length, petal width and petal length
    # Sepal Width Measurements (Coloured green)
    axes[0,0].hist(virginica_df['SepalWidthCm'], bins=20, color='g')
    axes[0,0].set_title('Sepal Width')

    # Sepal Length Measurements (Coloured red)
    axes[0,1].hist(virginica_df['SepalLengthCm'], bins=20, color='r')
    axes[0,1].set_title('Sepal Length')

    # Petal Width Measurements (Coloured magenta)
    axes[1,0].hist(virginica_df['PetalWidthCm'], bins=20, color='m')
    axes[1,0].set_title('Petal Width')

    # Petal Length Measurements (Coloured cyan)
    axes[1,1].hist(virginica_df['PetalLengthCm'], bins=20, color='c')
    axes[1,1].set_title('Petal Length')

    # Add a title to the plot
    plt.suptitle('Distribution of Iris Virginica Measurements')
    
    # Display the plot
    plt.show()

# Uncomment Below For Testing
#if __name__ == '__main__':
    #plot_setosa()
    #plot_versicolor()
    #plot_virginica()