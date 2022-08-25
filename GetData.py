import numpy as np
import csv
import matplotlib.pyplot as plt
import pandas as pd

filename = 'raw\\5-07-22_Test_Fire_Data_Raw.csv'

df = pd.read_csv(filename,names=['values'])
staticValues = df['values'][0:10]
maxVal = (np.max(staticValues))
data = df[df['values'] > maxVal]
data = data.reset_index(drop = True)
data.to_csv("cutData.csv")

print(data)
plt.plot(data)
plt.ylabel("Voltage (mV)")
plt.show()