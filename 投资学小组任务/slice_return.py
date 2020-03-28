# -*- coding:utf-8 -*-

import pandas as pd
from pandas.io.stata import StataReader
infilename = r"merge_2.dta"

outfile = 'out.csv'
if raw_input('are you sure to clear outputfile>>'+outfile+'<<(y/n)?')=='y':
    open(outfile,'w').close()
stata_data = StataReader(infilename, convert_categoricals=False)
data = stata_data.read()

col_n=['stkcd','time','rt_year','lnme','lev','size']
data = pd.DataFrame(data,columns = col_n)
data = data.dropna(axis=0)

def output(string):
    with open(outfile,'a') as f:
        f.write(string)




def slice(df_year):
    # df_year已经从低到高排序
    l_stk=df_year.iloc[:int(len(df_year)*0.3)]['stkcd'].tolist()
    m_stk=df_year.iloc[int(len(df_year)*0.3):int(len(df_year)*0.7)]['stkcd'].tolist()
    h_stk=df_year.iloc[int(len(df_year)*0.7):]['stkcd'].tolist()
    return h_stk,m_stk,l_stk


data_12_all=pd.DataFrame() # the data of December


dic={}
start_year=1995
stop_year=2018

for year in range(start_year,stop_year):
    timestring=str(year)+'-12'
    df_year=data[data.time==timestring]
    if year != start_year:
        slice_list = dic[year - 1]
        str_list=['h','m','l']
        for i in range(3): #lnme
            for j in range(3): #lev
                inter_list = list(set(slice_list[0][i]).intersection(set(slice_list[1][j])))
                need_stk=pd.DataFrame()
                for stk_id in inter_list:
                    need_stk = need_stk.append(df_year[df_year['stkcd']==stk_id],ignore_index=True)
                # print need_stk
                # print len(need_stk),'lev=',round(need_stk.mean(0)['lev'],3),'   lnme=',round(need_stk.mean(0)['lnme'],3)
                wei_rt=(need_stk['size']*need_stk['rt_year']).sum(0)/float(need_stk.sum(0)['size'])
                # print need_stk['size']*need_stk['rt_year']
                # print need_stk.sum(0)
                print year,str_list[i],str_list[j],'weighted_return=',wei_rt
                outstring=','.join([str(year),str_list[i],str_list[j],str(wei_rt)])+'\n'
                output(outstring)

    h1,m1,l1 = slice(df_year.sort_values(by='lnme'))
    h2,m2,l2 = slice(df_year.sort_values(by='lev'))
    dic[year]=[[h1,m1,l1],[h2,m2,l2]]
    # print dic

    data_12_all=data_12_all.append(df_year,ignore_index=True)



