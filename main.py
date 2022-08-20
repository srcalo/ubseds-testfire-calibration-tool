import csv
import matplotlib.pyplot as plt
import pandas as pd

filename = 'data\calibration-data-raw.csv'

with open(filename) as File:
    data = csv.reader(File)
    y = []
    for row in data:
        y.append(float(row[0]))

plt.plot(y)
plt.ylabel("Voltage (mV)")
plt.show()
