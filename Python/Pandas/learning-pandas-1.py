import pandas as pd

songs2=pd.Series([145,142,38,13],name="counts")
songs3=pd.Series([145,142,38,13],name='counts',index=['Paul','John','George','Ringo'])

nan_ser=pd.Series([2.0,None],index=['Ono','Clapton'])
