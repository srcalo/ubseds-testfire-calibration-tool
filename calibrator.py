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

    # Initialize variance 
    print(graph[0])
    prevMean = graph[0]
    print(prevMean)
    prevStdDev = 0
    varianceGraph = []
    count = 1
    variance = 0

    for x, y in enumerate(graph[:-1], 2):
        # If variance has increased beyond our threshold, record identified plateau using the mean
        # Then, reset running values and counter
        
        if(variance > MAXVARIANCE): # If variance is > THRESHOLD
            # Save average as plateau val
            # Reset prevMean and prevStdDev
            prevMean = y
            prevStdDev = 0
            count = 1 # Reset point counter
        
        count += 1 # Increase counter

        mean = prevMean + ((y - prevMean)/count)                # Calculate running mean
        stdDev = prevStdDev + (y - prevMean)*(y - mean)         # Calculate running standard deviation
        variance = stdDev/(count-1)                             # calculate running variance
        
        varianceGraph.append(variance)

        prevMean = mean
        prevStdDev = stdDev
    return varianceGraph



# Config
filename = 'data\\calibration-data-raw.csv'

graph = cutData(pd.read_csv(filename,names=['values']))
varGraph = findPlateau(graph['values'])
plt.figure(1)
plt.ylabel("Voltage (mV)")
plt.plot(graph)
plt.figure(2)
plt.plot(varGraph)
plt.show()