import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

'''
    This function takes in a pandas dataset and returns
    the trimmed data with some padding
'''
def cutData(dataset):


    staticValues = dataset['values'][0:1000] # takes the first ten data points
    maxVal = (np.max(staticValues)) # gets the maximum of those values
    booleanData = [dataset['values'] > maxVal] # creates an array of booleans that are True if they are > maxVal

    indexFirstPoint = 0 # index of the first True in booleanData
    indexLastPoint = 0 # index of the last True in booleanData
    for i, bool in enumerate(booleanData[0]): # iterates forwards through booleanData until it finds a true value then exits the loop
        if bool: 
            indexFirstPoint = i # saves the index of True value
            break
    for i, bool in enumerate(reversed(booleanData[0])): # iterates backwards through booleanData until it finds a true value then exits the loop
        if bool:
            indexLastPoint = np.size(booleanData) - i # saves the index of True value
            break
    
    cutData = dataset[indexFirstPoint-50:indexLastPoint+50] # creates the trimmed data with 50 points of padding on both sides
    cutData = cutData.reset_index(drop = True) # resets the indexes after trimming

    return cutData

if __name__ == "__main__":

    filename_Windows = 'raw\\5-07-22_Test_Fire_Data_Raw.csv'
    filename_MacOS = 'raw/5-07-22_Test_Fire_Data_Raw.csv'
    Testfire1_MacOS = '2022_2023_Data/TestFire1.csv'

    df = pd.read_csv(Testfire1_MacOS,names=['values']) # turns csv file into a usable dataset 
    
    data = cutData(df) # gets the cut data

    data.to_csv("cutData.csv") # creates a csv file with just the cut data

    # plots the cut data
    # plt.plot(df)
    # plt.ylabel("Voltage (mV)")
    plt.plot(data) 
    plt.ylabel("Voltage (mV)")
    plt.show()