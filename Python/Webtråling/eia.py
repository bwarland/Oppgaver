
import pandas as pd
import csv

GASPRODEIA=pd.read_json("/home/bwarland/Downloads/SeriesExport-09-15-2020-13-23-15.json")

eks=pd.Series([1,2,3,4],
              name='eks',
              index=['a','b','c','d'])
