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

df = pd.read_csv(sys.argv[1])

# convert pandas column to non-duplicated lists
dates = list(set(df[0].tolist())).sort()
symbols = list(set(df[1].tolist()))

# get first and last dates
dt_start = dates[0]
dt_end = dates[len(dates) - 1] + dt.timedelta(days=1)

dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

c_dataobj = da.DataAccess('Yahoo')
ls_keys = ['close']
key_data = c_dataobj.get_data(ldt_timestamps, symbols, ls_keys)
data = key_data[0]
