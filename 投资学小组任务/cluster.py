rf=[0.0198,0.019545,0.023952,0.024776,0.014746,0.022382,0.033243,0.041801,0.015083,0.024322,0.052163,0.043095,0.044432,0.049726,0.036939,0.029153,0.043631,0.039545]

data_list=[]
data_file= 'data/out2.csv'
data_lines=open(data_file).readlines()
for data_line in data_lines[1:]:
    data_infos=data_line.strip().split(',')
    data_list.append(data_infos)


sample_file= 'data/sample0.csv'
lines=open(sample_file).readlines()

hml = ['h', 'm', 'l']



def output(string,flag):
    with open('.\cluster\\'+flag+'.csv','a') as f:
        f.write(string)


def list_find(year,i,j,k):
    for data in data_list:
        if data[0]==str(year) and data[1]==hml[i] and data[2]==hml[j] and data[3]==hml[k]:
            return float(data[4])-rf[year-2001]

for i in range(3):
    for j in range(3):
        for k in range(3):# just like hhh,one file
            print(hml[i],hml[j],hml[k])
            outtext='T,RTRF,RMRF,SMB,HML,HZL\n'
            for index,line in enumerate(lines[1:]):
                infos=line.strip().split(',')
                year = index+2001
                RT_RF=list_find(year,i,j,k)
                infos[1]=str(RT_RF)
                print(infos)
                outtext+=','.join(infos)+'\n'
            output(outtext,str(hml[i])+str(hml[j])+str(hml[k]))
