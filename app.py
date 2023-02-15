import pandas_datareader as web
from datetime import datetime
import pandas as pd

start = datetime(2020,1,1)
end = datetime(2020,7,31)
stock = "GOOG"

df = web.DataReader(stock,'yahoo',start,end)
df.to_excel(f'stockdata_{stock}.xlsx')