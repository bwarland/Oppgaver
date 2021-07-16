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

george_dupe=pd.Series([10,7,1,22],
                      index=['1968','1969','1970','1970'],
                      name='George Songs')

sytti='1970'

g2=pd.Series({'1969':7,'1970':[1,22]},index=['1969','1970','1970'])

# for item in george_dupe.iteritems(): print(item)

george_dupe['1973']=11

'Paul' in songs3
145 in set(songs3)

# george_dupe.iloc[1]

# denne endrer ikke den opprinnelige serien
# sånn sett så er denne mer lik extend-metoden
# som Python-lister bruker
george_dupe.append(pd.Series({'1974':9}))

# set_value egenskapen fungerer ikke lenger, istedet kan man bruke
# iat[] eller at[]
# george_dupe.set_value('1974',9)
george_dupe.at['1974']=9

george=pd.Series([10,7,22],
                 index=['1968','1969','1970'],
                 name='George songs')

# george_dupe.index.is_unique
nett1=george>10
nett2=george>7
nett3=george<22
nett4=george>22

songs_66=pd.Series([3,None,11,9],
                   index=['George','Ringo','John','Paul'],
                   name='Counts')

songs_69=pd.Series([18,22,7,5],
                   index=['John','Paul','George','Ringo'],
                   name='Counts')

# for idx, value in songs_66.iteritems(): print(idx,value)
# for idx in songs_66.keys(): print(idx)
# songs_66+songs_69
# songs_66.fillna(0)+songs_69.fillna(0)


