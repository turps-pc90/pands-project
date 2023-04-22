# analysis.py
# This file will present the menu for four functions as laid out in assignment - based on the guide to create Python menus on this URL - https://computinglearner.com/how-to-create-a-menu-for-a-python-console-application/
# 1. Outputs summary of each variable to single text file
# 2. Saves a histogram of each variable to png file
# 3. Output a scatter plot of each pair of variables
# 4. Other function to be decided
# Author: Paul Callaghan

from summary import output_summary


menu_options = {
    1: 'Output Summary Of Each Variable',
    2: 'Save Histogram Of Each Variable', 
    3: 'Output Scatter Plot Of Each Pair Of Variables',
    4: 'To Be Decided',
    5: 'Exit',
}

def show_menu():
    for key in menu_options.keys():
        print(key, '-----', menu_options[key] )


def option1():
    output_summary()
    print("Option 1 has been selected. This has outputted a text file summarising the data for each of the iris species.")
    print("This file has been saved in the same location as this script.")

def option2():
    print('Handle option \'Option 2\'')

def option3():
    print('Handle option \'Option 3\'')

def option4():
    print('Handle option \'Option 4\'')



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