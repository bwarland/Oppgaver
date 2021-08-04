import pandas as pd
import numpy as np
import keyword
import matplotlib.pyplot as plt
# import seaborn as sb

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

# songs_66=pd.Series([3,None,11,9],
#                    index=['George','Ringo','John','Paul'],
#                    name='Counts')

# songs_69=pd.Series([18,22,7,5],
#                    index=['John','Paul','George','Ringo'],
#                    name='Counts')

# for idx, value in songs_66.iteritems(): print(idx,value)
# for idx in songs_66.keys(): print(idx)
# songs_66+songs_69
# songs_66.fillna(0)+songs_69.fillna(0)

navn=pd.Series(['George','John','Paul'])
# navn.str.lower()
# navn.str.findall('o')

def liten_skrift(val):
    return val.lower()

# navn.apply(liten_skrift)

s66=pd.Series([5.0,7.0,18.0,22.0],
              index=['Ringo','George','John','Paul'],
              name='c66')

s69=pd.Series([22.0,18.0,7.0,5.0],
              index=['John','Paul','George','Ringo'],
              name='c69')

# fig=plt.figure()
# s69.plot()
# s66.plot()
# s66.plot(kind='bar')
# s69.plot(kind='bar')

plt.legend()
# fig.savefig('/home/bwarland/GitHub/Oppgaver/Python/Pandas/.ex1.png')
# fig.savefig('/home/bwarland/GitHub/Oppgaver/Python/Pandas/.ex2.png')

data=pd.Series(np.random.randn(500),
               name='500 random')

# fig=plt.figure()
# ax=fig.add_subplot(111)
# data.hist()
fig.savefig('/home/bwarland/GitHub/Oppgaver/Python/Pandas/.ex3.png')

# fig=plt.figure()
# data.plot(kind='kde')

# fig.savefig('/home/bwarland/GitHub/Oppgaver/Python/Pandas/.ex4.png')