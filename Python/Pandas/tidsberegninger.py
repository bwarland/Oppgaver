# fra youtube

import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')

# ufo.head()

# ufo.dtypes

# ufo.Time.str.slice(-5,-3)

# ufo.Time.str.slice(-5,-3).astype(int).head()

# ufo['Time']=pd.to_datetime(ufo.Time)

ufo['Year']=ufo.Time.dt.year





