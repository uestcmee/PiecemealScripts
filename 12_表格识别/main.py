# encoding:utf-8

import requests
import base64
import time
import sys
def get_token():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=aVwgsapvt3RTwNC1Qr29QYvg&client_secret=hTvYzeE7LUKvaCPtSgY6iyQjmxCdcDW4'
    response = requests.get(host)
    if response:
        # print(response.json())
        print('获取token完成')
        return response.json()['access_token']


def send_img(token):
    '''
    表格文字识别(异步接口)
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/request"
    # 二进制方式打开图片文件
    f = open(img_path+IMG, 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    access_token = token
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print('图片发送完成')
        if 'result' in response.json():
            return(response.json()['result'][0]['request_id'])
        else:
            print(response.json())
            sys.exit(1)


def fetch_result(token,request_id):
    request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/get_request_result"
    # 二进制方式打开图片文件
    params = {"request_id": request_id,'result_type':'excel'}  # 可使用json或excel
    access_token = token
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        percent = response.json()['result']['percent']
        while(percent!=100):
            print('目前已完成{}%，请稍等'.format(percent))
            time.sleep(1)
            response=requests.post(request_url, data=params, headers=headers)
            percent = response.json()['result']['percent']
            # fetch_result(token,request_id) # 这样还要把递归里的response传出来，太麻烦了
        print('目前已完成{}%'.format(percent))
        result_data=response.json()['result']['result_data']
        print('\n',result_data)
        return(result_data)


def download_xls(url):
    print('开始下载xls')
    r = requests.get(url)
    with open(xls_path+"{}.xls".format(IMG.split('.')[0]), "wb") as code:
        code.write(r.content)
    print('下载完成')
    return 0
IMG=input('请输入图片名：')
img_path='./img/'
xls_path='./xls/'
# IMG='2015.png'
token=get_token() # 获取token
# request_id='18407915_1769790'
request_id=send_img(token) # 上传图片，获取request_id
url=fetch_result(token,request_id) # 获取结果url
download_xls(url) # 下载结果url

