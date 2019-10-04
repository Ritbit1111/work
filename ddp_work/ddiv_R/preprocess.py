import pandas as pd
import numpy as np

def preprocess(csv):
    df = pd.read_csv(csv, skiprows=47)#, nrows=90)
    N = df.shape[0]
    df = df.round(2)
    df = df.groupby('VOLTS').mean()
    df = df.sort_values(by=['VOLTS'])
    V = df.index
    df.to_csv('test.csv')
    return (V, df.AMPS)
