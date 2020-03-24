# coding:utf-8
import os


dir='C:\\Users\\zikep\\Desktop\\20200206发改委\\关于做好全国优化营商环境先进经验和典型做法复制\\昆明\\昆明经验总结'
movie_name = os.listdir(dir)
for temp in movie_name:
    print(temp)
    new_name=temp.replace('太原','昆明')
    os.rename(dir +'\\'+ temp, dir+'\\' + new_name)