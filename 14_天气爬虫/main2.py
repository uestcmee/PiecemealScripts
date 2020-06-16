import requests
url='http://www.tianqihoubao.com/lishi/yantai/month/{}{}.html'

for year in range(2011,2021):
    for month in range(1,13):

        if year==2020 and month>=6:
            continue
        # if (year,month) !=(2011,12) and (year,month) !=(2019,4):
        #     continue
        urls=url.format(year,str(month).zfill(2))
        print(urls)
        res=requests.get(urls)
        with open('./html2/{}_{}.html'.format(year,month),'wb') as f:
            f.write(res.text.encode('utf-8'))


# 2018 9
# 2019 3
# 2019 10
# 2020 5