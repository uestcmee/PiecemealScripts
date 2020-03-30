f=open('data/out3.csv', 'r')

lines=f.readlines()
info_list=[]
for line in lines[1:]:
    infos=line.strip().split(',')
    year=infos[0]
    lnme=infos[1]
    lnbm=infos[2]
    z_score=infos[3]
    rt=infos[4]
    info_list.append(infos)


outfile='smb_season.csv'
open(outfile,'w').close()
def output(string):
    with open(outfile,'a') as f:
        f.write(string)

zb_list=['lnme','lnbm','z_score']
for zb in range(1,4):
    for year in range(2004,2018):
        for season in range(4):
            if year==2004 and season==0:
                continue
            sum_h = 0
            sum_l = 0
            count_h=0
            count_l=0
            for i in range(len(info_list)):
                if info_list[i][0]==str(year)+'-'+str((season+1)*3).zfill(2):
                    if info_list[i][zb] == 'h':
                        sum_h += float(info_list[i][4])
                        count_h+=1
                    if info_list[i][zb] == 'l':
                        sum_l += float(info_list[i][4])
                        count_l+=1
                # print info_list[i][0], str(year) + '-' + str((season + 1) * 3)#.zfill(2)
            print sum_h ,sum_l,count_h,count_l

            try:
                print zb_list[zb-1],str(year),str((season+1)*3),round(sum_h/count_h,3),round(sum_l/count_l,3),'      ',round(sum_l/count_l-sum_h/count_h,3)
            except:
                print '\r',zb_list[zb-1],str(year),str((season+1)*3)
            outstring=zb_list[zb-1]+','+str(year)+'-'+str((season+1)*3).zfill(2)+','+str(sum_h/count_h)+','+str(sum_l/count_l)+','+str(sum_l/count_l-sum_h/count_h)+'\n'

            #outstring=','.join[zb_list[zb],str(year),str(sum_h/count_h),str(sum_l/count_l),str(sum_l/count_l-sum_h/count_h)]+'\n'
            output(outstring)
