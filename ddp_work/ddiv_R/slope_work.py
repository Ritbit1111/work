import numpy as np
import pandas as pd
from scipy import stats
from scipy import interpolate as ip
from matplotlib import pyplot as plt

#############################       Read from dataframe               ####################################
df1 = pd.read_csv('df/IV3.csv')
# print (df1.head())
#############################       Insert X and Y values here        ####################################
V = df1.V

I = df1.I
# I[30]=5
N = len(V)
print (f'The number of data points : {N}')
##########################################################################################################

# slope, intercept, c, d, std_err_for_slope = stats.linregress(x, y)

###################### Interpolation ####################
f_cubic = ip.interp1d(V,I, kind='cubic')
Vspline = np.arange(V[0], V[N-1], 0.1)
Ispline = f_cubic(Vspline)

##############################################################################

fig, [ax1, ax2] = plt.subplots(2,1)
ax1.set_xlabel('Voltages')
ax1.set_ylabel('Current')

ax1.plot(V,I,'or',label='Given Data')

ax2.plot(Vspline, Ispline, 'r', label='Interpolated cubic fit (Scipy)')
ax2.plot(V, I, 'b', label='Original data')
###################### TODO : Print all values here : slope +- delta, inter +- delta ######################
ax1.legend()
ax2.legend()
plt.show()
##########################################################################################################
