import xlrd
import numpy as np
from WindPy import w
w.start()

data = xlrd.open_workbook('portfolio.xlsx')

table = data.sheets()[0]

nrows = table.nrows

print 'nrows=', nrows
data_long = table.col_values(0)[1:]

for d in data_long:
    d=str(d)[:-2]
    dlen=len(d)
    if dlen!=6 and dlen!=0:
        d='0'*(6-dlen)+d
    print d
    if d[0]=='6':
        d+='.SH'
    else:
        d+='.SZ'
    print w.wsd(d, "close", "2018-01-29", "2018-02-26", "Fill=Previous")
    if raw_input('previous?')=='1':
        print w.wsd(d, "close", "2010-01-29", "2010-02-26", "Fill=Previous")
    if raw_input('go on?')!='1':
        break