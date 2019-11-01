x = np.linspace(0,100, 100)
y = np.where(x<40, 20, np.where(x<80, -(1/4)*(x-120), 0))
def func(x):
    return np.where(x<40, 20, np.where(x<80, -(1/4)*(x-120), 0))
print (func(60))
plt.plot(x,y)
plt.show()
