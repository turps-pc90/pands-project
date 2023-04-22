import pandas as pd
import time

timestamp = time.strftime("%d%m%Y-%H%M")

#with open(f'IrisDatasetSummary_{timestamp}.txt') as 
df = pd.read_csv('IrisDataset.csv')

print(df)

# Creating variables for each column
sep_l = df.SepalLengthCm
sep_w = df.SepalWidthCm
pet_l = df.PetalLengthCm
pet_w = df.PetalWidthCm
species = df.Species

print(sep_l)
