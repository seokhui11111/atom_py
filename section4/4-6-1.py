import pandas as pd
import xlrd
import openpyxl

#기본 읽기
# df=pd.read_excel("D:/atom_py/section4/excel_s1.xlsx")
# print(df)
# print(df.head())
# print(df.tail())

#행, footer 스킵
# df=pd.read_excel("D:/atom_py/section4/excel_s1.xlsx",skiprows=[0],skipfooter=45)
# print(df)

#헤더정의1
# df=pd.read_excel("D:/atom_py/section4/excel_s1.xlsx",header=0)
# print(df)
# print(list(df))

#헤더정의2
# df=pd.read_excel("D:/atom_py/section4/excel_s1.xlsx",skiprows=[0],header=None,names=["state",2018,2019,2020])
# print(df)

#특정 값 치환
df=pd.read_excel("D:/atom_py/section4/excel_s1.xlsx",skiprows=[0],header=0,na_values='...',converters={"2018":lambda w : w if w >60000 else None})
print(df)
# print(pd.isnull(df))
