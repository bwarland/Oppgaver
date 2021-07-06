import pandas as pd
import numpy as np

songs2=pd.Series([145,142,38,13],name="counts")
songs3=pd.Series([145,142,38,13],name='counts',index=['Paul','John','George','Ringo'])

nan_ser=pd.Series([2.0,None],index=['Ono','Clapton'])

class Foo:
    pass

ringo=pd.Series(['Richard','Starkey',13,Foo()])

numpy_ser=np.array([145,142,38,13])

mask=songs3>songs3.median()


# songs3[mask]

# numpy_ser[numpy_ser>np.median(numpy_ser)]
