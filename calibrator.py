import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sc
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
    graph = filter(graph)
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
            prevMean = -1
            prevStdDev = 0
            duration = 1
            start = x + CALCTHRESH

        duration += 1 # Increase counter
        if(duration > CALCTHRESH):

            if(prevMean < 0 or prevStdDev < 0):
                prevMean = y 

            mean = prevMean + ((y - prevMean)/(duration-CALCTHRESH))            # Calculate running mean
            stdDev = prevStdDev + (y - prevMean)*(y - mean)                     # Calculate running standard deviation
            variance = stdDev/(duration-CALCTHRESH)                             # calculate running variance
        
            prevMean = mean
            prevStdDev = stdDev

    
        varianceGraph.append(variance)

    return [results, varianceGraph]


def filter(input):
    return sc.signal.medfilt(input, FILTWIDTH)




if __name__ == "__main__": 

    # Config
    filename1_Windows = 'data/calibration-data-raw.csv'
    filename1_MacOS = 'data/calibration-data-raw.csv'
    filename2_Windows = 'Raw/5-07-22_Test_Fire_Calibration_2_Raw.csv'
    filename2_MacOS = 'Raw/5-07-22_Test_Fire_Calibration_2_Raw.csv'
    filename3_Windows = 'Raw/5-07-22_Test_Fire_Data_Raw.csv'
    filename3_MacOS = 'Raw/5-07-22_Test_Fire_Data_Raw.csv'
    Testfire1_MacOS = '2022_2023_Data/Calibration1.csv'

    graph = cutData(pd.read_csv(Testfire1_MacOS,names=['values']))
    graph = graph['values'].to_list()


    res = findPlateau(graph)


    plt.figure(1)
    plt.title("Raw Data")
    plt.xlabel("Time (ms)")
    plt.ylabel("Voltage (mV)")
    plt.plot(graph)

    plt.figure(2)
    plt.title("Variance")
    plt.xlabel("Time (ms)")
    plt.ylabel("Voltage (mV)")
    plt.plot(res[1])

    plt.figure(3)
    plt.title("Filtered data")
    plt.xlabel("Time (ms)")
    plt.ylabel("Voltage (mV)")
    plt.plot(filter(graph))
    print(f"Plateaus: {len(res[0])}")
    for i, val in enumerate(res[0], 1):
        plt.hlines(val[0], val[1], val[2], color="orange")
        print(f"Num: {i}, height: {val[0]}")

    plt.show()