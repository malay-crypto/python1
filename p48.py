import matplotlib.pyplot as pt
import numpy as np
import pickle
import csv
import pandas as pd

d={'name':['malay','raju','badal','dipak'],
    'salary':[10000,20000,30000,40000],
    

}

df=pd.DataFrame(d)
df['da']=df['salary']*50/100
df['total']=df['salary']+df['da']
df['perc']=0

print(df)
print("----------------------------")
df.loc[2,['name','salary']]=['akash',56000]
print("---------------")
print(df)