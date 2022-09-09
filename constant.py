''' findPlateau Config '''

DATARANGE = 100          # How many previous points to use as reference for averages
TIMETHRESHOLD = 300     # The minimum amount of time before another plateau can be recorded
MAXVARIANCE =  30      # Maximum variance of a set of points before the plateau no longer exists
CALCTHRESH = TIMETHRESHOLD/2        # How long to wait before calculating variance again
