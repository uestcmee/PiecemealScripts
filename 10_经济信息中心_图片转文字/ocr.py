# encoding:utf-8

import requests
import base64
import json

import os
def upload(img_name):
    '''
    通用文字识别（高精度版）
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/request"
    # 二进制方式打开图片文件
    f = open(img_name, 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    access_token = '[24.de468a64114d9056907820bd3224d23d.2592000.1583649709.282335-18407915]'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)

    if response:

        json_obj = response.json()
        result = json_obj['words_result']
        print(result)

        for item in result:
            print(item['words'].replace(' ', ''))


# dir= 'img'
# movie_name = os.listdir(dir)
# for temp in movie_name:
#     print('\n\n\n=================='+temp.replace('.jpg','')+'==================\n')
#     img_name='./img/'+temp
#     upload(img_name)
img_name='./img/2017.png'
upload(img_name)