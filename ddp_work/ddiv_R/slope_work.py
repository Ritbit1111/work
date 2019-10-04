import numpy as np
import pandas as pd
from scipy import interpolate as ip
from matplotlib import pyplot as plt
from preprocess import preprocess
from slope import get_slope
from get_spline import get_spline
from get_change_points import get_change_points
#############################       Read from dataframe               ####################################
df1 = pd.read_csv('df/IV3.csv')
V_ddiv = np.array(df1.V)
I_ddiv = np.array(df1.I)
scale_ddiv = np.max(V_ddiv)/np.max(I_ddiv)
# df1 = pd.read_csv('df_yogesh/dis.csv')
V_yog, I_yog = preprocess('df_yogesh/distorted.csv')
scale_yog = np.max(V_yog)/np.max(I_yog)
# df3 = pd.read_csv('iv_data_yogesh/b.csv')
# df4 = pd.read_csv('iv_data_yogesh/c.csv')
# df5 = pd.read_csv('iv_data_yogesh/d.csv')
# df6 = pd.read_csv('iv_data_yogesh/e.csv')
# df7 = pd.read_csv('iv_data_yogesh/f.csv')
# print (df1.head())
#############################       Insert X and Y values here        ####################################

###################### Interpolation ####################

V_spl_yog, I_spl_yog = get_spline(V_yog, I_yog, 500)

slope_yog = get_slope(I_spl_yog, V_spl_yog, regression_length = 10)
slope_yog_sc = get_slope(I_spl_yog, V_spl_yog, regression_length = 5, scale = scale_yog)

double_der_yog = get_slope(slope_yog, V_spl_yog[0:len(slope_yog)])
grad_yog = np.gradient(slope_yog)

error = 0.023
change_points_yog = get_change_points(V_spl_yog, slope_yog, error)
print(change_points_yog)
##############################################################################

V_spl_ddiv, I_spl_ddiv = get_spline(V_ddiv, I_ddiv, 500)

slope_ddiv = get_slope(I_spl_ddiv, V_spl_ddiv, regression_length = 15)
slope_ddiv_sc = get_slope(I_spl_ddiv, V_spl_ddiv, regression_length = 5, scale= scale_ddiv)

double_der_ddiv = get_slope(slope_ddiv, V_spl_ddiv[0:len(slope_ddiv)])
grad_ddiv = np.gradient(slope_ddiv)

error = 0.01
change_points_ddiv = get_change_points(V_spl_ddiv, slope_ddiv, error)
print(change_points_ddiv)
##############################################################################

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(12,10))

ax1.plot(V_spl_yog, I_spl_yog, 'b',label='Spline fit for Survey data')
ax1.plot(V_spl_yog[0:len(slope_yog)], slope_yog, 'r',label='Slope of survey data')
ax1.plot(V_spl_yog[0:len(grad_yog)], grad_yog, 'y',label='Change of slope')
for p in change_points_yog:
    ax1.axvline(p)

# ax1.plot(V_spl_yog[0:-6][0:-6], double_der_yog, 'g',label='Double derivative')
# ax1.plot(V_yog, I_yog, 'xk',label='Given data')
ax2.plot(V_spl_yog[0:len(slope_yog_sc)], slope_yog_sc, 'r',label='Slope of survey data')
ax2.plot(V_spl_yog[0:len(grad_yog)], 10*scale_yog*grad_yog, 'y',label='Change of slope')

# ax2.plot(V, I, 'or', label='Original data')
# ax2.plot(V_ddiv, I_ddiv, 'xk',label='Given data')
ax3.plot(V_spl_ddiv, I_spl_ddiv, 'b', label='Spline fit for DDIV data')
ax3.plot(V_spl_ddiv[0:len(slope_ddiv)], slope_ddiv, 'r',label='Slope of DDIV data')
ax3.plot(V_spl_ddiv[0:len(grad_ddiv)], grad_ddiv, 'y',label='Change of slope')
for p in change_points_ddiv:
    ax3.axvline(p)
# ax3.plot(V_spl_ddiv[0:-6][0:-6], double_der_ddiv, 'g',label='Double derivative')
ax4.plot(V_spl_ddiv[0:len(slope_ddiv_sc)], slope_ddiv_sc, 'r',label='Slope of DDIV data')
ax4.plot(V_spl_ddiv[0:len(grad_ddiv)], 10*scale_ddiv*grad_ddiv, 'y',label='Change of slope')
###################### TODO : Print all values here : slope +- delta, inter +- delta ######################
ax1.set_xlabel('Voltages')
ax1.set_ylabel('Current')
ax2.set_xlabel('Voltages')
ax2.set_ylabel('Current')
ax1.legend()
ax2.legend()
plt.draw()
plt.waitforbuttonpress(0)
plt.close(fig)
##########################################################################################################
