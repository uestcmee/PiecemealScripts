import xlrd
import numpy as np

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

