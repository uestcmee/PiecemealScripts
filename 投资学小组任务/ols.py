# coding:utf-8
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from pandas import read_csv
import os
import  matplotlib.pyplot as plt

path = './cluster2/'
files = os.listdir(path)
out_file = 'ols_out.txt'
open(out_file, 'w').close()
for file in files:
    if str(file)[-3:]=='csv':
        pass
    else:
        continue
    print file
    infilename = str(file)
    data = read_csv(path + infilename)
    data = data.dropna(axis=0)
    est = smf.ols(formula='RTRF ~ RMRF + SMB + HML + HZL ', data=data)
    res = est.fit()
    print res.summary()
    with open(out_file, 'a') as f:
        f.write('\n'*5+str(file) + '\n'*5)
        f.write(str(res.summary()) + '\n')
    # print res.params
    # print 'R2:',res.rsquared
    # p_hzl=res.pvalues[-1]
    # if p_hzl<0.01:
    #     xz='***'
    # elif p_hzl<0.05:
    #     xz='**'
    # elif p_hzl<0.1:
    #     xz='*'
    # else:
    #     xz=''
    # print 'p(HZL):',res.pvalues[-1],4,xz
    # print res.f_test("HZL=0")
    # plt.scatter(data.RTRF,data.SMB)
    # plt.show()
