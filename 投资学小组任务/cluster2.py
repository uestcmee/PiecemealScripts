# rf=[0.0198,0.019545,0.023952,0.024776,0.014746,0.022382,0.033243,0.041801,0.015083,0.024322,0.052163,0.043095,0.044432,0.049726,0.036939,0.029153,0.043631,0.039545]
rf = [0, 0.006149, 0.006795, 0.006211, 0.005487, 0.002862, 0.002777, 0.003651, 0.004426, 0.005031, 0.006098, 0.006796,
      0.007076, 0.007465, 0.008229, 0.010436, 0.011235, 0.01122, 0.010878, 0.008485, 0.003389, 0.003065, 0.004118,
      0.004495, 0.004775, 0.005263, 0.006319, 0.007928, 0.011793, 0.011895, 0.014441, 0.013994, 0.013217, 0.011161,
      0.009304, 0.009444, 0.009722, 0.0107, 0.011737, 0.012239, 0.013896, 0.012951, 0.01171, 0.011207, 0.012297,
      0.009168, 0.007838, 0.007702, 0.007386, 0.007273, 0.007079, 0.007416, 0.010127, 0.011172, 0.010847, 0.01147,
      0.011746, 0.010484, 0.007779, 0.007099]
data_list = []
data_file = 'out3.csv'
data_lines = open(data_file).readlines()
for data_line in data_lines[1:]:
    data_infos = data_line.strip().split(',')
    data_list.append(data_infos)

sample_file = 'sample1.csv'
lines = open(sample_file).readlines()

hml = ['h', 'm', 'l']


def output(string, flag):
    with open('./cluster2/' + flag + '.csv', 'a') as f:
        f.write(string)


def outputfake(string, flag):
    pass


def list_find(year, season, i, j, k):
    time_str = str(year) + '-' + str((season + 1) * 3).zfill(2)
    print time_str

    for data in data_list:
        if data[0] == time_str and (data[1], data[2], data[3]) == (hml[i], hml[j], hml[k]):
            return float(data[4]) - rf[(year - start_year) * 4 + season]


start_year = 2004
for i in range(3):
    for j in range(3):
        for k in range(3):  # just like hhh,one file
            print hml[i], hml[j], hml[k]
            open('./cluster2/'+str(hml[i]) + str(hml[j]) + str(hml[k])+ '.csv','w').close()
            outtext = 'T,RTRF,RMRF,SMB,HML,HZL\n'
            for index, line in enumerate(lines[1:]):
                infos = line.strip().split(',')
                year = index / 4 + start_year
                season = index % 4
                if index < 3:
                    year = start_year
                    season = index + 1

                else:
                    year = ((index - 3) / 4) + 1 + start_year
                    season = (index - 3) % 4
                print 'year:', year, 'season:', season
                RT_RF = list_find(year, season, i, j, k)
                infos[1] = str(RT_RF)
                # print infos
                outtext += ','.join(infos) + '\n'
            output(outtext, str(hml[i]) + str(hml[j]) + str(hml[k]))
