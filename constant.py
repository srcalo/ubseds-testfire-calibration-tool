''' 
    findPlateau Config
    All time values are in ms    
'''
SAMPLERATE = 1      # Rate that data was recorded in ms (recorded every SAMPLERATE ms)
FILTWIDTH =  3500*(1//SAMPLERATE)+1      # The size of the filter window for the median filter. Must be an odd number and in ms
TIMETHRESHOLD = 200*(1//SAMPLERATE)     # The minimum amount of time before another plateau can be recorded
MAXVARIANCE =  999999999999999     # Maximum variance of a set of points before the plateau no longer exists
CALCTHRESH = (TIMETHRESHOLD*(1//SAMPLERATE))/2        # How long to wait before calculating variance again


CALCRATE = 10*(1//SAMPLERATE)      # How often values will be calculated (Calc value every X points)