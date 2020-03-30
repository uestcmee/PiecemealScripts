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

def stkinput(stk_id):
    mouse.position=(520,150)
    mouse.click(button=Button.left)
    for num in range(6):
        win32api.keybd_event(int(stk_id[num])+48,0,0,0)
        win32api.keybd_event(int(stk_id[num])+48,0,win32con.KEYEVENTF_KEYUP,0)
        # time.sleep(0.05)
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


def mcontext_copy():
    mouse.position = (600,900)
    mouse.click(button=Button.left)
    copy_paste('a')
    copy_paste('c')
    print('text copied ')
    mouse.position = (500,400)
    mouse.click(button=Button.left)
    copy_paste('a')
    copy_paste('v')
    # print('text pasted ')


stk_id='002668'

while(True):
    input()

    instring=pyperclip.paste()
    outstring=instring.replace(' ','').replace('\n','').replace('\r','')
    #print('input:',instring)
    pyperclip.copy(outstring)
    print('title:',pyperclip.paste())

    stkinput(stk_id)

    title_input()

    mcontext_copy()

    time.sleep(0.5)