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



plt.plot(graph)
plt.ylabel("Voltage (mV)")
plt.show()

'''
    Finds the values at which the graph plateaus by checking if 
    a certain number of points on the graph remains nearly constant
    for long enough
'''
results = [] # dictionary of results formatted as [value, startTime, duration]

value = 0
startTime = 0
duration = 0

yPrev = graph[0]
avg = 0
count = 0

for x, y in enumerate(graph[:-1]):
    dif = y - yPrev
    



plt.plot(graph)
plt.ylabel("Voltage (mV)")
plt.show()