''' findPlateau Config '''
FILTWIDTH =  301        # The size of the filter window for the median filter. Must be an odd number
TIMETHRESHOLD = 200     # The minimum amount of time before another plateau can be recorded
MAXVARIANCE =  30      # Maximum variance of a set of points before the plateau no longer exists
CALCTHRESH = TIMETHRESHOLD/2        # How long to wait before calculating variance again
