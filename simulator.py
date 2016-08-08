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
dt_first = dates[0]
dt_last = dates[len(dates) - 1] + dt.timedelta(days=1)
