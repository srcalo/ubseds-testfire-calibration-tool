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
results = [] # dictionary of results formatted as [value, startTime, duration]

value = 0
startTime = 0
duration = 0

yPrev = graph[0]
avg = 0
variance = 0
count = 0

for x, y in enumerate(graph[:-1]):
    
    



plt.plot(graph)
plt.ylabel("Voltage (mV)")
plt.show()