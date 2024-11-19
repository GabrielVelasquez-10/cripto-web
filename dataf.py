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

def crypto_value(index):
    return float(data[index]['Close'][-1:])

def cryto_calulator(in_index, out_index, in_number):
    return (float(in_number) * crypto_value(in_index))/crypto_value(out_index)

def cryto_all_values():
    dataall = {}
    for index in names_index:
        dataall[index] = data[index]['Close'][-1:]
    dataall = pd.DataFrame(dataall).fillna(0).sum()
    return dataall
dataall = cryto_all_values()