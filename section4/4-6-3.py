import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randint(500,1000,size=(100,4),cloumns=[2015,2016,2017]))
print(df)

#csf index,header(True,False)
#excel index(None),header(True,False)
df.to_excel("D:atom_py/section4/res1.xlsx",index=None,header=True)
