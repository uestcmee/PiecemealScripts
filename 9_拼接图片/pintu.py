# coding:utf-8
import os
from PIL import Image

path = "./"
imagefile = []
for  files in os.listdir(path):
    if files[-3:]=='JPG':
        imagefile.append(Image.open('./'+files))

N=len(imagefile)
UNIT_WIDTH = imagefile[0].size[1] # 图像的高
UNIT_LENGHT = imagefile[0].size[0]
target = Image.new('RGB', (UNIT_LENGHT, UNIT_WIDTH*N))  # 纵向拼接，高度变为n倍，宽度不变

left = 0
right = UNIT_WIDTH
for image in imagefile:
    # The box argument is either
    # a 2-tuple giving the upper left corner,
    # a 4-tuple defining the left, upper, right, and lower pixel coordinate
    # target.paste(image, (0, left, UNIT_LENGHT , right))    # 左上角参数，右下角参数
    target.paste(image,(0,left)) # 只用左上角定位，横向为x轴
    left += UNIT_WIDTH # 从上往下拼接，左上角的纵坐标递增
    # right += UNIT_WIDTH #左下角的纵坐标也递增　
    quality_value = 100
    target.save(path+'/result.jpg', quality = quality_value)
