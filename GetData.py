import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def cutData(dataset):
    staticValues = df['values'][0:10]
    maxVal = (np.max(staticValues))
    booleanData = [df['values'] > maxVal]
    print(type(booleanData))

    i = 0
    indexFirstPoint = 0
    indexLastPoint = 0
    while indexFirstPoint == 0:
        if booleanData[0][i] == True:
            indexFirstPoint = i
        else:
            i += 1
    i = np.size(booleanData) - 1
    while indexLastPoint == 0:
        if booleanData[0][i] == True:
            indexLastPoint = i
        else:
            i -= 1
    
    cutData = df[indexFirstPoint-50:indexLastPoint+50]
    cutData = cutData.reset_index(drop = True)
    return cutData

filename = 'raw\\5-07-22_Test_Fire_Data_Raw.csv'

df = pd.read_csv(filename,names=['values'])

data = cutData(df)

data.to_csv("cutData.csv")

print(data)
plt.plot(data)
plt.ylabel("Voltage (mV)")
plt.show()