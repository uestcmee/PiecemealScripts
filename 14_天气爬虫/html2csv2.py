from bs4 import BeautifulSoup
for year in range(2017,2021):
    for month in range(1,13):
        if year==2020 and month>=6:
            continue
        print(year,month)
        with open('./html2/{}_{}.html'.format(year, month), 'r',encoding='utf-8') as f:
            text=f.read()
            soup=BeautifulSoup(text,'lxml')
            table=soup.find_all('table')[0]
            # except:
            #     print('error',year,month)
            lines=table.find_all('tr')[1:]
            for line in lines:
                infos=line.text.strip().replace(' ','').split('\n')
                print(infos)
                date=infos[0]
                high=infos[8][:-1]
                low=infos[10][:-1]
                infos=[date,high,low]
                print(infos)
                with open('out2.csv','a') as f2:
                    f2.write(','.join(infos)+'\n')
                    f2.close()
            f.close()



