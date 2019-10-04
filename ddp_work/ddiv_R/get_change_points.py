import numpy as np

def get_change_points(V, slope, error):
    N = len(slope)
    points = []
    for i in range (N):
        s1 = slope[i]
        s2 = slope[i+1] if i<N-1 else s1
        if s1<0 and np.absolute(s1) - np.absolute(s2) > error:
            print (f'Point found at V = {V[i]}')
            points.append(V[i])
    return points
