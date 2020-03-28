# coding:utf-8
import pyperclip
import time
import win32con
import win32api
from pynput.mouse import Button
from pynput.mouse import  Controller as mController
from pynput.keyboard import Key
from pynput.keyboard import Controller as kController

mouse = mController()
keyboard= kController()

# 以前的程序遗留的一块，这次并没有用到，当时是为什么混着用pynput和win32api来着
# 当时写杭电oj的爬虫的时候是怎么输入来着，好像是浏览器对话框输入
def stkinput(stk_id):
    for num in range(0,len(stk_id)):
        # 按下数字键并释放 因为0是对应48号键码，所以需要加48
        win32api.keybd_event(int(stk_id[num])+48,0,0,0)
        win32api.keybd_event(int(stk_id[num])+48,0,win32con.KEYEVENTF_KEYUP,0)
        # time.sleep(0.05)
    # 13号键码为enter
    win32api.keybd_event(13,0,0,0)
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.05)
    print('stk_ID input ')

def copy_paste(flag):
    keyboard.press(Key.ctrl)
    time.sleep(0.1)
    keyboard.press(flag)
    time.sleep(0.1)
    keyboard.release(flag)
    time.sleep(0.1)
    keyboard.release(Key.ctrl)
    time.sleep(0.1)

def title_input():
    mouse.position=(320,50)
    mouse.click(button=Button.left)
    copy_paste('v')
    print('title pasted ')


def click(coor_list):
    mouse.position=(coor_list[0],coor_list[1])
    mouse.click(button=Button.left)
    time.sleep(0.1)

import xlrd
# 键盘监听
from pynput.keyboard import Key,Listener
def on_press(key):
    if key == Key.enter:
        print('you press Enter')
        listener.stop()
    elif key==Key.esc:
        return False
    else:
        return 1
        #return False #按键不是enter,停止监视
def on_release(key):
    if key == Key.enter:
        print('you release Enter')

search_coor=[280/2,70/2]
input_coor=[630/2,1780/2]

book=xlrd.open_workbook('grade&qq.xlsx')
sheet1=book.sheet_by_index(0)
print(sheet1.name,'rows=',sheet1.nrows,'cols=',sheet1.ncols)
for i in range(38,sheet1.nrows):
    std_info=sheet1.row(i)

    std_qq=str(int(std_info[3].value))
    name=std_info[1].value
    grade=round((std_info[2].value))
    #print(grade)

    click(search_coor)
    pyperclip.copy(std_qq)
    print(std_qq)
    copy_paste('v')

    # keyboard.press(Key.enter)
    # time.sleep(0.1)
    #keyboard.release(Key.enter)
    # 监听键盘按键
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    click(input_coor)
    text=name+'同学您好，你本学期的高等数学的平时成绩为'+str(grade)+'分，如果对于成绩有异议可以联系我。\n祝期末顺利！'
    print(text)
    pyperclip.copy(text)
    copy_paste('v')
    # click(send_coor)
    # time.sleep(1)
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

