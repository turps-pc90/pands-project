# analysis.py
# This file will present the menu for four functions as laid out in assignment - based on the guide to create Python menus on this URL - https://computinglearner.com/how-to-create-a-menu-for-a-python-console-application/
# 1. Outputs summary of each variable to single text file
# 2. Saves a histogram of each variable to png file
# 3. Output a scatter plot of each pair of variables
# 4. Other function to be decided
# Author: Paul Callaghan

from summary import output_summary
from histogram import *
from scatterplot import * 
from other import *

menu_options = {
    1: 'Output Summary Of Each Variable',
    2: 'Save Histogram Of Each Variable', 
    3: 'Output Scatterplot Of Sepals (Width & Length) Or Petals (Width & Length)',
    4: 'Seaborn Varities',
    5: 'Exit',
}

# Main menu for user
def show_menu():
    for key in menu_options.keys():
        print(key, '-----', menu_options[key] )

# Sub menu for user if option 2 selected
def sub_menu2():
        sub_menu_options = {
            1: 'Iris Setosa',
            2: 'Iris Versicolor', 
            3: 'Iris Virginica',
            4: 'Exit',    
        }
        print("Please select a which species to display a histogram for:")
        for key in sub_menu_options.keys():
            print(key, '-----', sub_menu_options[key] )

        sub_option = int(input("Enter your choice by selecting the corresponding number: "))
        if sub_option == 1:
            # Call the plot_setosa() function from histogram.py for option 1
            plot_setosa()
            print("Iris Setosa selected")
        elif sub_option == 2:
            # Call the plot_versicolor() function from histogram.py for option 2
            plot_versicolor()
            print("Iris Versicolor selected")
        elif sub_option == 3:
            # Call the plot_virginica() function imported from histogram.py for option 3
            plot_virginica()
            print("Iris Virginica selected")
        elif sub_option == 4:
            # Close menu
            exit()
        else:
            print("Invalid option. Please select a number between 1 and 3.")

# Sub menu for user if option 3 selected
def sub_menu3():
        sub_menu_options = {
            1: 'Sepals',
            2: 'Petals', 
            3: 'Exit',    
        }
        print("Please select whether you would like to show the scatterplot for sepal measurements or petal measurements:")
        for key in sub_menu_options.keys():
            print(key, '-----', sub_menu_options[key] )

        sub_option = int(input("Enter your choice by selecting the corresponding number: "))
        if sub_option == 1:
            # Call the scatterplot_sepals function from scatterplot.py for option 1
            scatterplot_sepals()
            print("Sepals selected")
        elif sub_option == 2:
            # Call the scatterplot_petals function from scatterplot.py for option 2
            scatterplot_petals()
            print("Petals selected")
        elif sub_option == 3:
            # Close the menu
            exit()
        else:
            print("Invalid option. Please select a number between 1 and 3.")

# Sub menu for user if option 4 selected
def sub_menu4():
        sub_menu_options = {
            1: 'Facet Grid',
            2: 'Violin Grid', 
            3: 'Pair Plot',  
            4: 'Exit'  
        }
        print("Please select which of the Seaborn grids you would like to try:")
        for key in sub_menu_options.keys():
            print(key, '-----', sub_menu_options[key] )

        sub_option = int(input("Enter your choice by selecting the corresponding number: "))
        if sub_option == 1:
            # Call the iris_facetgrid function from other.py for option 1
            iris_facetgrid()
            print("Facet Grid selected")
        elif sub_option == 2:
            # Call the iris_violin function from other.py for option 2
            iris_violin()
            print("Violin Grid selected")
        elif sub_option == 3:
            # Call the iris_pairplot function from other.py for option 3
            iris_pairplot()
            print("Pair Plot selected")
        elif sub_option == 4:
            # Close the menu
            exit()
        else:
            print("Invalid option. Please select a number between 1 and 4.")


def option1():
    output_summary()
    print("Option 1 has been selected. This has outputted a text file summarising the data for each of the iris species.")
    print("This file has been saved in the same location as this script.")
    print("Function complete")
    print("- - - - - - - - - - - - - - - -")

def option2():
    print("Option 2 has been selected.")
    sub_menu2()
    print("- - - - - - - - - - - - - - - -")
    print(" ")

def option3():
    print("Option 3 has been selected.")
    sub_menu3()
    print("- - - - - - - - - - - - - - - -")
    print(" ")

def option4():
    print("Option 4 has been selected.")
    sub_menu4()
    print("- - - - - - - - - - - - - - - -")
    print(" ")


if __name__ == '__main__':
    while(True):
        show_menu()
        option = ''
        try:
            option = int(input('Enter your choice by selecting the corresponding number: '))
        except:
            print('You have not selected a number from the menu.')
        # Validate menu selection
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            print('You have selected to close the application.')
            print('Thank you.')
            exit()
        else:
            print('Invalid option. Please select a number between 1 and 5.')