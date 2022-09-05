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
    results = []    # dictionary of plateau values formatted as [value, startTime, endTime, duration]
    varianceGraph = []
    value = startTime = duration = 0

    # Initialize statistics 
    duration = 1
    start = 0
    prevMean = graph[0]
    prevStdDev = 0
    variance = 0

    

    for x, y in enumerate(graph[:-1], 2):
        # If variance has increased beyond our threshold, record identified plateau using the mean
        # Then, reset running values and counter
        if(not len(results) or variance > MAXVARIANCE and duration > TIMETHRESHOLD):
            results.append([prevMean, start, x, duration])# Save average as plateau val
            
            # Reset stats
            prevMean = y
            prevStdDev = 0
            duration = 1
            start = x

        duration += 1 # Increase counter
        if(duration > CALCTHRESH+1):
            mean = prevMean + ((y - prevMean)/(duration-CALCTHRESH))            # Calculate running mean
            stdDev = prevStdDev + (y - prevMean)*(y - mean)                     # Calculate running standard deviation
            variance = stdDev/((duration-CALCTHRESH)-1)                         # calculate running variance
        
            prevMean = mean
            prevStdDev = stdDev

    
        varianceGraph.append(variance)

    return [results, varianceGraph]



# Config
filename_Windows = 'data\\calibration-data-raw.csv'
filename_MacOS = 'data/calibration-data-raw.csv'

graph = cutData(pd.read_csv(filename_MacOS,names=['values']))
res = findPlateau(graph['values'])


plt.figure(1)
plt.ylabel("Voltage (mV)")

plt.plot(graph)
print(f"Plateaus: {len(res[0])}")
for i, val in enumerate(res[0], 1):
    plt.hlines(val[0], val[1], val[2], color="orange")
    print(f"Num: {i}, height: {val[0]}")
    # plt.hlines(val[0], val[2] - 200, val[2] + 200, color="red")
    # plt.vlines(val[2], val[0] - 200, val[0] + 200, color="red")




plt.figure(2)
plt.plot(res[1])
plt.show()