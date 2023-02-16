## Description

This script downloads stock data from Yahoo Finance using the `pandas_datareader` library, for a specified time period and stock ticker. It then saves the data as an Excel file in the current working directory.

## Dependencies

- `pandas_datareader`
- `pandas`
- `datetime`

## Usage

1. Replace `start` and `end` variables with the desired start and end dates in the `datetime` format.
2. Replace `stock` variable with the desired stock ticker.
3. Run the script.

## Example

```python
import pandas_datareader as web
from datetime import datetime
import pandas as pd

start = datetime(2020,1,1)
end = datetime(2020,7,31)
stock = "GOOG"

df = web.DataReader(stock,'yahoo',start,end)
df.to_excel(f'stockdata_{stock}.xlsx')
