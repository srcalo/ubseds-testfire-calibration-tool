''' 
    findPlateau Config
    All time values are in ms    
'''
SAMPLERATE = 10      # Rate that data was recorded in ms (recorded every SAMPLERATE ms)
FILTWIDTH =  int(3500*(1/SAMPLERATE)+1)      # The size of the filter window for the median filter. Must be an odd number and in ms
TIMETHRESHOLD = int(2500*(1/SAMPLERATE))     # The minimum amount of time before another plateau can be recorded
MAXVARIANCE =  int(500*(1/SAMPLERATE))     # Maximum variance of a set of points before the plateau no longer exists
CALCTHRESH = int((TIMETHRESHOLD*(1/SAMPLERATE))/2)        # How long to wait before calculating variance again

CALCRATE = int(10*(1/SAMPLERATE))      # How often values will be calculated (Calc value every X points)

ENDTHRESH = CALCRATE+1