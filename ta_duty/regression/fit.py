import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

x = np.linspace(1, 5, num=5, endpoint=True)
y=np.array([2,4,1,6,8])
xbar = np.mean(x)
ybar = np.mean(y)

# coeff = np.polyfit(y,x,1)
# fit = coeff[1]*x + coeff[0]

xnew = np.linspace(-1, 5, num=7, endpoint =True)
A = x-xbar;print (A) 
B = y-ybar;print (B) 
num = np.sum(A*B)
denom = np.sum(A*A)
slope = num/denom
intercept = ybar - slope * xbar
# print (f'Slope is {num/denom} compared to np.polyfit slope {coeff[1]}')
# print (intercept, f'compared to ployfit {coeff[0]}')
ynew = slope*xnew + intercept

slp, intr, r, p, s = stats.linregress(x,y)
y_scipy = slp*xnew + intr


bill = np.array([34, 108, 64, 88, 99, 51])
tip = np.array([5, 17, 11, 8, 14, 5])
a,b,c,d,std_dev_for_slope = stats.linregress(bill, tip)
print (a, b, c, d, std_dev_for_slope)

print (f't alpha by 2 for for 20 is :{stats.t.ppf(0.005, 18)}')



fig, ax1 = plt.subplots(1,1) #, sharex=True)
# ax1.plot(x, fit, '--y', label='Numpy Polyfit'),
ax1.plot(xbar, ybar, 'xm', label='Centroid')
ax1.plot(x, y, '--.k', label='Given Data')
ax1.plot(xnew, ynew, '--g', label='Formulae Fit')
ax1.plot(xnew, y_scipy, '.r', label='Scipy Fit')
ax1.set_title('Straight Line')
ax1.set_xlabel('X Values')
ax1.set_ylabel('Y Values')
plt.legend()
plt.show()
