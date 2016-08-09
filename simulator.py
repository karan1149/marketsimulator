# Using QuantSoftwareToolKit and concommitant libraries
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import sys

orders = pd.read_csv(sys.argv[1])

# convert pandas column to non-duplicated lists
dates = list(set(orders[0].tolist())).sort()
symbols = list(set(orders[1].tolist()))

# get first and last dates
dt_start = dates[0]
dt_end = dates[len(dates) - 1] + dt.timedelta(days=1)

dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

c_dataobj = da.DataAccess('Yahoo')
ls_keys = ['close']
key_data = c_dataobj.get_data(ldt_timestamps, symbols, ls_keys)
data = key_data[0]

full_dates = [dt_start + datetime.timedelta(days=x) for x in range(0, (dt_end-dt_start).days)]

# create empty dataframe for trade matrix
a = np.zeros(shape=(len(full_dates), len(symbols)))
trades = pd.DataFrame(a, columns=symbols)
trades.set_index(full_dates)

casha = np.zeros(shape=(len(full_dates), 1))
cash = pd.DataFrame(casha)
cash.set_index(full_dates)
cash[dt_start] = sys.argv[0]

# iterate through trades to create trade matrix
for index, row in orders.iterrows():
    amount = row[3]
    if row[2] == "SELL":
        amount = amount * -1
    trades[row[0], row[1]] = trades[row[0], row[1]] + amount
    cash[row[0], 0] = cash[row[0], 0] - amount * data[row[0], row[1]]

holdings = trades.cumsum(axis = 0)
cash = cash.cumsum(axis = 0)

total_stocks = holdings.dot(data)
portfolio = total_stocks + cash
