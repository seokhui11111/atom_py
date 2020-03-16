import pandas as pd
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding = "utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding = "utf-8")

df1=pd.read_csv("D:/atom_py/section4/csv_s2.csv",header=0)
print(df1)

print(df1['State'])
df1['State'] = df1['State'].str.replace(' ',' | ')
print(df1)

df1['Avg']=df1[['2018','2019','2020']].mean(axis=1).round(2)
