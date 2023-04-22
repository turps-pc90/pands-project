# summary.py
# The Group By function is something I would use frequently in my job when working with SQL Server Management Studio 
# and used the guide here (https://realpython.com/pandas-groupby/#the-hello-world-of-pandas-groupby)
# to help with this function
# Author: Paul Callaghan

import pandas as pd
import time

timestamp = time.strftime("%d%m%Y-%H%M")


df = pd.read_csv('IrisDataset.csv')

# Creating variables for each column
sep_l = df.SepalLengthCm
sep_w = df.SepalWidthCm
pet_l = df.PetalLengthCm
pet_w = df.PetalWidthCm
species = df.Species


# Using Pandas built-in Group By function to group the measurements by iris species
grouped = df.groupby('Species')
min_vals = grouped.min()
max_vals = grouped.max()

# Create function to be imported to analysis.py
def output_summary():
    # Open .txt file with timestamp to reflect when script was run
    with open(f'IrisDatasetSummary_{timestamp}.txt', 'w') as file:
        # Loop through each row of CSV and write string with the values of variables created above but grouping by species. 
        for i in species.unique():
            # Loop through minimum and maximum values for each variable grouped by species type. The .loc requires column names from csv file. 
            sep_l_min = min_vals.loc[i, 'SepalLengthCm']
            sep_l_max = max_vals.loc[i, 'SepalLengthCm']
            sep_w_min = min_vals.loc[i, 'SepalWidthCm']
            sep_w_max = max_vals.loc[i, 'SepalWidthCm']
            pet_l_min = min_vals.loc[i, 'PetalLengthCm']
            pet_l_max = max_vals.loc[i, 'PetalLengthCm']
            pet_w_min = min_vals.loc[i, 'PetalWidthCm']
            pet_w_max = max_vals.loc[i, 'PetalWidthCm']
            output = f"For the {i} species, the sepal length ranges from {sep_l_min}cm to {sep_l_max}cm. The sepal width ranges from {sep_w_min}cm to {sep_w_max}cm. The petal length ranges from {pet_l_min}cm to {pet_l_max}cm. The petal width ranges from {pet_w_min}cm to {pet_w_max}cm."
            # Puts line between each outputted string
            file.write(output + '\n')
            
