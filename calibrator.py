import csv
import matplotlib.pyplot as plt
import numpy as np

# Config
filename = 'data\\calibration-data-raw.csv'
timeThresh = 0  # The minimum amount of time that a plateau exists before its counted
maxVariance = 0 # Maximum difference between points before a plataeu no longer exists


with open(filename) as File:
    data = csv.reader(File)
    graph = []
    for row in data:
        graph.append(float(row[0]))

graphDiff = np.diff(graph)

plt.plot(graphDiff)
plt.ylabel("Voltage (mV)")
plt.show()

'''
    Finds the values at which the graph plateaus by checking if 
    a certain number of points on the graph remains nearly constant
    for long enough
'''
for x, y in enumerate(graphDiff[:-1]):
    x = 0
    



plt.plot(graphDiff)
plt.ylabel("Voltage (mV)")
plt.show()