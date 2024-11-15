import os
import pandas as pd

csv_files = os.listdir('csv_files')
names_index = []

def csv_data():
    data = {}
    for name_files in csv_files:
        n_index = name_files[0:len(name_files)-4]
        names_index.append(n_index)
        data[n_index] = pd.read_csv(f'csv_files/{name_files}')
    return data
data = csv_data()