import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from GetData import cutData

# Config
filename = 'data\\calibration-data-raw.csv'
timeThresh = 0  # The minimum amount of time that a plateau exists before its counted
maxVariance = 0 # Maximum difference between points before a plataeu no longer exists


graph = cutData(pd.read_csv(filename))


'''
    Finds the values at which the graph plateaus by checking if 
    a certain number of points on the graph remains nearly constant
    for long enough
'''
def findPlateau():
    results = [] # dictionary of results formatted as [value, startTime, duration]

    value = 0
    startTime = 0
    duration = 0

    yPrev = graph[0]
    avg = graph=[0]
    avgSq = avg**2
    variance = 0
    count = 1

    for x, y in enumerate(graph[:-1]):
        count = count


'''
    Calculates an average when adding a value to an existing average
'''
def calculateAverage(oldAverage, newValue, newN):
    return oldAverage + (newValue - oldAverage)/newN

plt.plot(graph)
plt.ylabel("Voltage (mV)")
plt.show()