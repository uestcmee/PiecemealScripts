# 获取debt/GDP数据

主要就用`pic_crawler.py`和`mg_process_all`两个文件就可以，`img_process`之前调试的时候用的


1. 使用`pic_crawler.py`网页获取图片和比率的最大最小值信息,图片存储在`img`文件夹，最大最小等信息存储在`infos.csv`中
2. `img_process_all`通过对图片进行简单的处理，获取坐标点信息，从而对数据进行估算