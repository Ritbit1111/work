import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

#############################       Insert X and Y values here        ####################################

x = np.array([34, 51, 64, 88, 99, 108])
y = np.array([5, 5, 11, 8, 14, 17])
N = len(x)
##########################################################################################################

slope, intercept, c, d, std_err_for_slope = stats.linregress(x, y)
y_pred = slope*x + intercept

xbar = np.mean(x)
ybar = np.mean(y)
x_res = x-np.mean(x)
y_res = y-y_pred

se = np.sum(y_res*y_res)
mse = se/(N-2)
Sxx = np.sum(x_res * x_res)

##############################       SLOPE CONFIDANCE INTERVAL    ########################################  

ci_percent = 95
alpha = (100-ci_percent)/100
t = stats.t.ppf(alpha/2, N-2)

std_err_slope = np.sqrt(mse/Sxx) 
slope_CI = [slope + t*std_err_slope, slope - t*std_err_slope]
intercept_rel = [ybar - slope_CI[0]*xbar, ybar - slope_CI[1]*xbar]

y_min_slope = slope_CI[0]*x+intercept_rel[0]
y_max_slope = slope_CI[1]*x+intercept_rel[1]

#####################################     INTERCEPT CONFIDANCE INTERVAL   #################################

std_err_intercept = np.sqrt(mse*(1/N + xbar*xbar/Sxx)) 
intercept_CI = [intercept + t*std_err_intercept,intercept - t*std_err_intercept]
y_min_intercept = slope*x+intercept_CI[0]
y_max_intercept = slope*x+intercept_CI[1]

##########################################    Printing Area   #############################################

print ('Slope     : {} +- {}'.format(np.around(slope, 4), np.around(t*std_err_slope,4)))
print ('Intercept : {} +- {}'.format(np.around(intercept, 4), np.around(t*std_err_intercept,4)))

##########################################    Plotting Area   #############################################

fig, ax = plt.subplots(1,1)
ax.set_xlabel('X values')
ax.set_ylabel('Y values')

ax.axvline(xbar, ls='--', color='#C0C0C0', label = 'X Bar')
ax.axhline(ybar, ls='--', color='#C0C0C0',label = 'Y Bar')

ax.plot(x,y,'or',label='Given Data')
ax.plot(x, y_pred, '-og', label='Linear fit (Scipy)')
###################### TODO : Print all values here : slope +- delta, inter +- delta ######################
ax.plot(x, y_min_slope, '--', color='#65F608', label = f'Min slope')
ax.plot(x, y_max_slope, '--', color='#65F608', label = f'Max slope')
ax.plot(x, y_min_intercept, '--', color='#000000', label = f'Min intercept')
ax.plot(x, y_max_intercept, '--', color='#000000', label = f'Max intercept')
ax.fill_between(x, y_min_slope, y_max_slope, color = '#eaede2')
ax.fill_between(x, y_min_intercept, y_max_intercept, color = '#b4d55b', alpha=0.3)
ax.legend()
plt.show()
##########################################################################################################
