#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import xlrd
from numpy import *


def get_r(data0):
    for i in range(len(data0) - 1):
        data0[i] = (data0[i + 1] - data0[i]) / data0[i]
    return data0[:-1]
# read the xlsx file
data=xlrd.open_workbook('data.xlsx')
table=data.sheets()[0]
nrows=table.nrows

data_index=table.col_values(1)[1:]  # 大盘指数数据
data0=[]
for d in data_index:
    data0.append(round(d,2))
print '大盘指数：',data0

data_a= table.col_values(2)[1:]  # 股票A数据
data=[]
for d in data_a:
    data.append(round(d,2))
print '股票A的数据:',data


# calculate the withdraw
index_j = np.argmax(np.maximum.accumulate(data) - data)  # 结束位置
print u'结束位置',index_j
index_i = np.argmax(data[:index_j])  # 开始位置
print u'开始位置',index_i
d = data[index_j] - data[index_i]  # 最大回撤
print u'最大回撤',d


# 绘制图像
plt.figure(1)
plt.subplot(211)
plt.plot(data)
plt.plot([index_i, index_j], [data[index_i], data[index_j]], 'o', color="r", markersize=10)
plt.subplot(212)
plt.plot(data0)
plt.show()


data0=get_r(data0)
data=get_r(data)

data_cov=np.cov([data,data0])
print '协方差矩阵:',data_cov
print 'beta:',data_cov[0,1]/(data_cov[1,1])



