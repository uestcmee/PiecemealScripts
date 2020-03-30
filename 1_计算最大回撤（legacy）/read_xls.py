import xlrd
import numpy as np
data=xlrd.open_workbook('data.xlsx')

table=data.sheets()[0]

nrows=table.nrows

data_origin= table.col_values(2)[1:]

data0=[]
for d in data_origin:
    data0.append(round(d,2))

data=data0
print data
print(np.maximum.accumulate(data))
