import numpy as np
import pandas as pd
from scipy import stats
from scipy import interpolate as ip
from matplotlib import pyplot as plt
from gekko import GEKKO


#############################       Read from dataframe               ####################################
df1 = pd.read_csv('df/IV3.csv')
# print (df1.head())
#############################       Insert X and Y values here        ####################################

# x = np.array([34, 51, 64, 88, 99, 108, 115])
# y = np.array([5, 5, 11, 8, 14, 17, 20])
# N = len(x)

# print (df1.tail())
x = np.array(df1.V)
N = len(x)
xnew = np.arange(x[0], x[N-1], 0.1)
# print (logx)
y = np.array(df1.I)
# y[N-1] = 0.0001
# print (logy)
print (f'The number of data points : {N}')

m = GEKKO()
m.x = m.Param(value=xnew)
m.y = m.Var()
m.cspline(m.x, m.y, x, y)
m.options.IMODE = 2
m.solve(disp=False)
##########################################################################################################
# slope, intercept, c, d, std_err_for_slope = stats.linregress(x, y)
# y_pred = slope*x + intercept


##############################################################################

###################### Interpolation ####################
f = ip.interp1d(x,y)
f_quadratic = ip.interp1d(x,y, kind='quadratic')
f_cubic = ip.interp1d(x,y, kind='cubic')

tck = ip.splrep(x, y, s=0)
ynew = ip.splev(xnew, tck, der=0)
ius = ip.InterpolatedUnivariateSpline(x, y)
rbf = ip.Rbf(x,y)
##################### Spline #########################################################
##############################################################################

fig, [ax1, ax2] = plt.subplots(2,1)
ax1.set_xlabel('X values')
ax1.set_ylabel('Y values')

ax1.plot(x,y,'r',label='Given Data')
ax1.plot(m.x, m.y, 'b',label='Gekko')
# ax1.plot(np.exp(logxnew), y_cubic, 'b', label='Log cubic')
ax1.plot(xnew, f_cubic(xnew), '--g', label='cubic')
# ax1.plot(xnew, ynew_cubic, 'b', label='Interpolate cubic fit (Scipy)')

ax2.plot(x, y, 'g', label='Given data')
ax2.plot(xnew, ynew, 'r', label='Interpolated cubic fit (Scipy)')
ax2.plot(xnew, ius(xnew), 'k', label='Ius')
# ax2.plot(xnew, rbf(xnew), 'b', label='RBF')
###################### TODO : Print all values here : slope +- delta, inter +- delta ######################
ax1.legend()
ax2.legend()

plt.draw()
# plt.pause(1) # <-------
# input("<Hit Enter To Close>")
plt.waitforbuttonpress(0)
plt.close(fig)
##########################################################################################################
