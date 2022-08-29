import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from GetData import cutData
from constant import *




'''
    findPlateau(graph: pandas.dataframe)

    Finds the values at which the graph plateaus by checking if 
    a certain number of points on the graph remains nearly constant
    for long enough

    Running versions of values is when you calculate the value (i.e. mean) without having to maintain a total sum
    This way we can do our calculations in one sweep and not multiple
    
    Running variance algorithm based on the following blog post
    https://www.johndcook.com/blog/standard_deviation/
'''
def findPlateau(graph):
    results = []    # dictionary of plateau values formatted as [value, startTime, duration]
    value = startTime = duration = 0

    # Initialize variance values
    prevMean = graph[0]
    prevStdDev = 0
    
    count = 1

    for x, y in enumerate(graph[:-1]):

        mean = prevMean + (y - prevMean)/x                  # Calculate running mean
        stdDev = prevStdDev + (y - prevMean)*(y - mean)     # Calculate running standard deviation
        variance = stdDev/(x-1)                             # calculate running variance


        prevMean = mean
        prevStdDev = stdDev
    return results



# Config
filename = 'data\\calibration-data-raw.csv'

graph = cutData(pd.read_csv(filename))

plt.plot(graph)
plt.ylabel("Voltage (mV)")
plt.show()