import numpy as np
import pandas as pd
from scipy import stats
from scipy import interpolate as ip
from matplotlib import pyplot as plt

#############################       Read from dataframe               ####################################
df1 = pd.read_csv('df/IV1.csv')
print (df1.head())
#############################       Insert X and Y values here        ####################################

x = np.array([34, 51, 64, 88, 99, 108, 115])
y = np.array([5, 5, 11, 8, 14, 17, 20])
N = len(x)

x = df1.V
y = df1.I
N = len(x)
print (f'The number of data points : {N}')
##########################################################################################################

slope, intercept, c, d, std_err_for_slope = stats.linregress(x, y)
y_pred = slope*x + intercept


##############################################################################

###################### Interpolation ####################
f = ip.interp1d(x,y)
f_quadratic = ip.interp1d(x,y, kind='quadratic')
f_cubic = ip.interp1d(x,y, kind='cubic')

xnew = np.arange(x[0], x[N-1], 0.1)
ynew = f(xnew)
ynew_quadratic = f_quadratic(xnew)
ynew_cubic = f_cubic(xnew)

##################### Spline #########################################################
f_uni = ip.UnivariateSpline(x,y, s=7)
f_uni_nos = ip.UnivariateSpline(x,y)
y_uni = f_uni(xnew)
y_uni_nos = f_uni_nos(xnew)
##############################################################################

fig, [ax1, ax2] = plt.subplots(2,1)
ax1.set_xlabel('X values')
ax1.set_ylabel('Y values')

ax1.plot(x,y,'or',label='Given Data')
# ax1.plot(x, y_pred, '-og', label='Linear fit (Scipy)')
# ax.plot(xnew, ynew, '--k', label='Interpolate 1 fit (Scipy)')

ax1.plot(xnew, ynew_cubic, 'b', label='Interpolate cubic fit (Scipy)')
ax1.plot(xnew, ynew_quadratic, 'k', label='Interpolate quadratic fit (Scipy)')
# ax.plot(xnew, ynew_zero, '--b', label='Interpolate 1 fit (Scipy)')

ax2.plot(x, y, 'or', label='Given data')
ax2.plot(xnew, y_uni, '--b', label='Univariate Cubic fit s=3')
ax2.plot(xnew, y_uni_nos, 'k', label='Univariate Cubic fit default s')
ax2.plot(xnew, ynew_cubic, 'r', label='Interpolated cubic fit (Scipy)')
# for i in range(10):
#     f_uni_s = ip.UnivariateSpline(x,y,s=0.5*i)
#     ax2.plot(xnew, f_uni_s(xnew), 'k' , label=f'Univar. s={i}')
###################### TODO : Print all values here : slope +- delta, inter +- delta ######################
ax1.legend()
ax2.legend()
plt.show()
##########################################################################################################
