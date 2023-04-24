# histogram.py
# This function creates a histogram of each variable and basing the function on the plottask.py task
# Copied functions from summary.py to calculate averages of petal and sepal measurements for each of three iris species - 
# iris-setosa, iris-virginica and iris-versicolor
# Author: Paul Callaghan

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('IrisDataset.csv')

# Creating a menu for user input. Copying same format as analysis.py page
menu_options = {
    1: 'Iris Setosa',
    2: 'Iris Versicolor', 
    3: 'Iris VIrginica',
    4: 'Exit',    
}


def show_menu():
    for key in menu_options.keys():
        print(key, '-----', menu_options[key] )


# Splitting three species into three functions to prompt user selection for which histogram to see
# Defining function to show Iris Setosa
def plot_setosa():
    # Selecting data for Iris Setosa species
    setosa_df = df[df['Species'] == 'Iris-setosa']

    # Creating subplots for each measurement, 2 rows and 2 columns with figsize of 8 x 8 inches
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8,8))

    # Creating histogram for sepal width, sepal length, petal width and petal length
    # Sepal Width Measurements (Coloured green)
    axes[0,0].hist(setosa_df['SepalWidthCm'], bins=10, color='g')
    axes[0,0].set_title('Sepal Width')

    # Sepal Length Measurements (Coloured red)
    axes[0,1].hist(setosa_df['SepalLengthCm'], bins=10, color='r')
    axes[0,1].set_title('Sepal Length')

    # Petal Width Measurements (Coloured magenta)
    axes[1,0].hist(setosa_df['PetalWidthCm'], bins=10, color='m')
    axes[1,0].set_title('Petal Width')

    # Petal Length Measurements (Coloured cyan)
    axes[1,1].hist(setosa_df['PetalLengthCm'], bins=10, color='c')
    axes[1,1].set_title('Petal Length')

    # Add a title to the plot
    plt.suptitle('Distribution of Iris Setosa Measurements')
    
    # Display the plot
    plt.show()

def plot_versicolor():
    print("Yet to be built")


def plot_virginica():
    print("Yet to be built")



# Create a list of variables for average sepal lengths and widths for each species
#avg_sep_l = [df.loc[df['Species'] == species, 'SepalLengthCm'].mean() for species in df['Species'].unique()]
#avg_sep_w = [df.loc[df['Species'] == species, 'SepalWidthCm'].mean() for species in df['Species'].unique()]
#avg_pet_l = [df.loc[df['Species'] == species, 'PetalLengthCm'].mean() for species in df['Species'].unique()]
#avg_pet_w = [df.loc[df['Species'] == species, 'PetalWidthCm'].mean() for species in df['Species'].unique()]





if __name__ == '__main__':
    while(True):
        show_menu()
        option = ''
        try:
            # Prompt user to input number to select which iris species to plot. 
            option = int(input('Enter your choice by selecting the corresponding number: '))
        except:
            print('You have not selected a number from the menu.')
        # Validate menu selection
        if option == 1:
            plot_setosa()
        elif option == 2:
            plot_versicolor()
        elif option == 3:
            plot_virginica()
        elif option == 4:
            print('You have selected to close the application.')
            print('Thank you.')
            exit()
        else:
            print('Invalid option. Please select a number between 1 and 4.')