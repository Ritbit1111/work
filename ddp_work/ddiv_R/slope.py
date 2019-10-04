import numpy as np
from scipy import stats

def get_slope(I, V, regression_length = 5, scale = 1):
    N = len(I)
    max_V = np.max(V)
    max_I = np.max(I)
    slope = []
    for i in range(N-1-regression_length):
        Iarr = I[i:i+regression_length]
        Varr = V[i:i+regression_length]
        sl, i, c, d, se = stats.linregress(Varr, Iarr)
        slope.append(sl)
    return scale*np.array(slope)
