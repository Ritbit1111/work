import numpy as np
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt

df = pd.read_csv('data/data_rk_09-22@19.25.18.csv')
N= df.shape[0]
df['Index1'] = df.Index+1
df['F(t)'] = (df.Index1-1)/(N-0.4)
df['Y'] = -np.log(1-df['F(t)'])
print (df.head())
print (df.tail())
