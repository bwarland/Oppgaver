import pandas as pd
import numpy as np
import datetime as dt

index=pd.date_range("7/1/2021",periods=10)
s=pd.Series(np.random.randn(5), index=['a','b','c','d','e'])
df=pd.DataFrame(np.random.randn(10,3),index=index, columns=['A','B','C'])
lang_s=pd.Series(np.random.randn(1000))
df2=pd.DataFrame(np.random.randn(10,3),index=index, columns=['A','B','C'])

s2=pd.Series(np.arange(10))

# div,rem=divmod(s2,3)

# idx=pd.Index(np.arange(10))
# div,rem=divmod(idx,3)

# dti=pd.to_datetime(  ["1/1/2021",np.datetime64("1/1/2021"),datetime.datetime(2021,1,1)])

idx=pd.date_range('2021-07-01',periods=5,freq='H')
