# -*- coding:utf-8 -*-

import pandas as pd
from pandas.io.stata import StataReader

infilename = r"season_merge.dta"
outfile = 'out3.csv'
open(outfile,'w').close()

stata_data = StataReader(infilename, convert_categoricals=False)
data = stata_data.read()
data = pd.DataFrame(data)

col_n=['stkcd','time','rt_season','z_score','lnme','lnbm','size']
data = pd.DataFrame(data,columns = col_n)
data = data.dropna(axis=0)
# print data.sort_values(by='time')


def output(string):
    with open(outfile,'a') as f:
        f.write(string)


def slice(df_year):
    # df_year已经从低到高排序
    l_stk=df_year.iloc[:int(len(df_year)*0.3)]['stkcd'].tolist()
    m_stk=df_year.iloc[int(len(df_year)*0.3):int(len(df_year)*0.7)]['stkcd'].tolist()
    h_stk=df_year.iloc[int(len(df_year)*0.7):]['stkcd'].tolist()
    return h_stk,m_stk,l_stk


dic={}
start_year = 2004
stop_year = 2018

for year in range(start_year,stop_year):
    for half in range(4):
        timestring=str(year)+'-'+str((half+1)*3).zfill(2)
        print 'timestring',timestring
        df_year=data[data.time==timestring]
        print 'the length of this season: ',len(df_year)
        if year != start_year or half != 0:
            slice_list = dic[year*4+half-1]
            str_list=['h','m','l']
            for i in range(3): #lnme
                for j in range(3): #lnbm
                    for k in range(3):#z_score
                        inter_list = list(set(slice_list[0][i]).intersection(set(slice_list[1][j])).intersection(set(slice_list[2][k])))
                        #print inter_list
                        need_stk=pd.DataFrame()
                        for stk_id in inter_list:
                            need_stk = need_stk.append(df_year[df_year['stkcd']==stk_id],ignore_index=True)
                        print need_stk

                        wei_rt=(need_stk['size']*need_stk['rt_season']).sum(0)/float(need_stk.sum(0)['size'])

                        print str(year)+'-'+str((half+1)*3),str_list[i],str_list[j],str_list[k],'weighted_return=',wei_rt
                        outstring=','.join([str(year)+'-'+str((half+1)*3),str_list[i],str_list[j],str_list[k],str(wei_rt)])+'\n'
                        output(outstring)


        h1,m1,l1 = slice(df_year.sort_values(by='lnme'))#  市值
        h2,m2,l2 = slice(df_year.sort_values(by='lnbm'))# 账面市值比
        h3,m3,l3 = slice(df_year.sort_values(by='z_score'))
        dic[year*4+half]=[[h1,m1,l1],[h2,m2,l2],[h3,m3,l3]]


