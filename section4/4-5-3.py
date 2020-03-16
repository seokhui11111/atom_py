import pandas as pd
import numpy as np

#랜덤으로 DataFrame 생성 (100행 4열)
# df=pd.DataFrame(np.random.randint(0,100,size=(100,4)),columns=list("ABCD"))
df=pd.DataFrame(np.random.randint(0,100,size=(100,4)),columns=["One","Two","Three","Four"])
# df=pd.DataFrame(np.random.randn(100,4),columns=list("ABCD"))
# print(df)

#CSV 쓰기
df.to_csv("D:/atom_py/section4/result1.csv",index=False,header=False)
print("commit")
