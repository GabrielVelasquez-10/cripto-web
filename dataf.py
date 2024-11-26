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

#intento de convertir un str a fecha y poder trabajarlo 
def date_visualization():
    dats={}
    for date in names_index:
        dats[date]= data[date]['Date']
    dats= {key: pd.to_datetime(value, format='ISO8601') for key, value in dats.items()} 
    return dats
dats=date_visualization()