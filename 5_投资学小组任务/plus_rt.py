import pandas as pd
from pandas.io.stata import StataReader

infilename = r"season_merge.dta"

stata_data = StataReader(infilename, convert_categoricals=False)
data = stata_data.read()
data = pd.DataFrame(data)

col_n=['stkcd','time','rtnew']#,'z_score','lnme','lnbm','size']
data = pd.DataFrame(data,columns = col_n)
data = data.dropna(axis=0)
print(data.sort_values(by='time'))

outfile='rt_seaon.csv'
open(outfile,'w').close()
def output(string):
    with open(outfile,'a') as f:
        f.write(string)



for year in range(2001,2018):
    print(year)
    for season in range(4):
        print (season)
        ts0=str(year)+'-'+str((season)*3+1).zfill(2)
        ts1=str(year)+'-'+str((season)*3+2).zfill(2)
        ts2=str(year)+'-'+str((season)*3+3).zfill(2)

        df_season = data[(data.time == ts0)|(data.time==ts1)|(data.time==ts2)]
        print (df_season)
        stk_list = df_season['stkcd'].tolist()
        stk_list=list(set(stk_list))
        for stk in stk_list:
            stk_seaon=df_season[df_season.stkcd==stk]
            #print stk_seaon
            stk_rt=stk_seaon['rtnew'].tolist()
            if len(stk_rt)!=3:
                continue
            stk_seson_rt=(1+stk_rt[0])*(1+stk_rt[1])*(1+stk_rt[2])-1
            #print stk_seson_rt
            outstring=stk+','+str(year)+'-'+str((season+1)*3)+','+str(stk_seson_rt)
            output(outstring+'\n')






