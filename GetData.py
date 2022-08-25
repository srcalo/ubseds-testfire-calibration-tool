import numpy as np
import csv
import matplotlib.pyplot as plt
import pandas as pd

filename = 'raw\\5-07-22_Test_Fire_Data_Raw.csv'

df = pd.read_csv(filename,names=["values"])
print(df)
plt.plot(df)
plt.ylabel("Voltage (mV)")
plt.show()