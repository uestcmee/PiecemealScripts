from bs4 import BeautifulSoup
import requests

# 国家名称列表，稍微修改了一些以符合网页需要
country_list='''ARGENTINA
AUSTRIA
AUSTRALIA
BELGIUM
BRAZIL
CANADA
SWITZERLAND
CHINA
CZECH REPUBLIC
GERMANY
DENMARK
SPAIN
FINLAND
FRANCE
UNITED KINGDOM
HONG KONG
INDONESIA
IRELAND
INDIA
ITALY
JAPAN
SOUTH KOREA
LUXEMBOURG
MEXICO
MALAYSIA
NETHERLANDS
NORWAY
NEW ZEALAND
PERU
PHILIPPINES
POLAND
PORTUGAL
ROMANIA
RUSSIA
SWEDEN
SINGAPORE
THAILAND
TAIWAN
SOUTH AFRICA
'''.replace(' ','-').split('\n')[:-1]


# 详情页的url，在详情页中获取最大最小值和国家简写
con_url='https://tradingeconomics.com/{}/government-debt-to-gdp'
# 图像的获取url，可以直接获得最大时间长度的走势图
img_url='https://d3fy651gv2fhd3.cloudfront.net/charts/government-debt-to-gdp.png?s={}debt2gdp&v=202008042300V20200716&d1=19200830&type=candlestick'



# 获取图像并保存
def fetch_img(short): #short 为国家简写，因为获取图片的url中需要用到国家简写
    res=requests.get(img_url.format(short))
    with open('./img/{}.jpg'.format(country),'wb') as f:
        f.write(res.content)


# 单个国家详情页代码
def country_page(country):
    res=requests.get(con_url.format(country))
    with open('./html/{}.html'.format(country),'wb') as f:
        f.write(res.text.encode('utf-8'))
        f.close()


info_dic={}

# 下面的部分因为一步一步做的，所以循环里的三个部分我是分开运行的，不过一起运行应该也可以
for country in country_list:
    print(country)

    # # 1. 获取网页并保存，方便后面提取最大最小值和图片url
    # country_page(country)

    # # 2. 获取图片
    # with open('html/{}.html'.format(country),encoding='utf-8') as f:
    #     text=f.read()
    #     soup = BeautifulSoup(text,'lxml')
    #     country_short=re.findall('(?<=gdp\.png\?s=).{2,5}(?=debt2gdp)',text)[0]
    #     print(country_short)
    #     fetch_img(country_short)


    # 3. 获取最大最小值
    with open('html/{}.html'.format(country),encoding='utf-8') as f:
        info_list = [] # 用来存储详情页中的几个数据
        text=f.read()
        soup = BeautifulSoup(text,'lxml')
        div=soup.find_all('div',id='ctl00_ContentPlaceHolder1_ctl00_IndicatorSummaryUC_PanelDefinition')[0]
        for one in div.find_all('td'):
            info_list.append(one.text)
        info_dic[country]=info_list

print(info_dic)

import pandas as pd
pd.DataFrame(info_dic).to_csv('infos.csv') # 直接保存了，清洗放在了另一个文件中
