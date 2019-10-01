import numpy as np
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt

points=100
shape = 1
scale = 100
np.random.seed(0)
T = scale * np.random.weibull(shape, points)
a = np.log(T)
# b = a*(0.9+0.2*np.random.uniform(0,1,points))
b = 0.9*a+0.2*(a*np.random.uniform(0,1,points))
T_with_noise = np.exp(b)
# s_with_noise = np.round(s + np.random.normal(0, noise_level, points), 6)
df = pd.DataFrame({'Values':T_with_noise})
df2 = df.sort_values('Values')
df2['Sample#'] = df2.index + 1
df2.index = range(points)
df2.index.name = 'Index' 
df2 = df2[['Sample#', 'Values']]
N= df.shape[0]
df['Index1'] = df.index+1
df['F(t)'] = (df.Index1-0.3)/(N+0.4)
df['Y'] = -np.log(1-df['F(t)'])
#############################       Insert X and Y values here        ####################################

x = np.array(df.Values)
y = np.array(df['Y'])
# x = np.array([34, 108, 64, 88, 99, 51])
# y = np.array([5, 17, 11, 8, 14, 5])
##########################################################################################################

slope, intercept, c, d, std_dev_for_slope = stats.linregress(x, y)
y_pred = slope*x + intercept
print (f'Slope is {slope} \nand intercept is {intercept}')
print (f'Error in slope is {std_dev_for_slope}')
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
std_err = np.sqrt(mse/Sxx) 

t = stats.t.ppf(alpha/2, N-2)
slope_CI = [slope + t*std_err,slope - t*std_err]
print (slope_CI)
intercept_rel = [ybar - slope_CI[0]*xbar, ybar - slope_CI[1]*xbar]
y_min_slope = slope_CI[0]*x+intercept_rel[0]
y_max_slope = slope_CI[1]*x+intercept_rel[1]

#####################################     INTERCEPT CONFIDANCE INTERVAL   #################################
std_err_intercept = np.sqrt(mse*(1/N + xbar*xbar/Sxx)) 
print (f'Error in intercept is {std_err_intercept}')
t = stats.t.ppf(alpha/2, N-2)
intercept_CI = [intercept + t*std_err_intercept,intercept - t*std_err_intercept]
y_min_intercept = slope*x+intercept_CI[0]
y_max_intercept = slope*x+intercept_CI[1]

##########################################    Plotting Area   #############################################

fig, ax = plt.subplots(1,1)
ax.set_xlabel('X values')
ax.set_ylabel('Y values')
ax.axvline(xbar, ls='--', color='#C0C0C0', label = 'X Bar')
ax.axhline(ybar, ls='--', color='#C0C0C0',label = 'Y Bar')
ax.plot(x,y,'or',label='Given Data')
ax.plot(x, y_pred, '-og', label='Linear fit (Scipy)')
###################### TODO : Print all values here : slope +- delta, inter +- delta ######################
ax.plot(x, y_min_slope, '--', color='#65F608', label = f'Min slope {slope_CI[0]}')
ax.plot(x, y_max_slope, '--', color='#65F608', label = f'Max slope {slope_CI[1]}')
ax.plot(x, y_min_intercept, '--', color='#000000', label = f'Min intercept {intercept_CI[0]}')
ax.plot(x, y_max_intercept, '--', color='#000000', label = f'Max intercept {intercept_CI[1]}')
ax.fill_between(x, y_min_slope, y_max_slope, color = '#eaede2')
ax.fill_between(x, y_min_intercept, y_max_intercept, color = '#b4d55b', alpha=0.3)
ax.legend()
plt.show()
##########################################################################################################
