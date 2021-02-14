from pandas_datareader import wb
from datetime import datetime

startdato=datetime(2000,1,1)
sluttdato=datetime(2019,12,31)
indicator_id='NY.GDP.PCAP.KD'

GDP_cap=wb.download(indicator=indicator_id,start=startdato,end=sluttdato,country=['US','CN'])
