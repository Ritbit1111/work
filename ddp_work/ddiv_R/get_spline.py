from scipy import interpolate as ip
import numpy as np

def get_spline(V, I, points):
    V_spl = np.linspace(V[0], V[-1], points)
    f_cubic = ip.interp1d(V,I, kind='cubic')
    I_spl = f_cubic(V_spl)
    return (V_spl, I_spl) 
