# 键盘输入
# 为了快速下载法律意见书




import pynput.mouse as mouse
from pynput.keyboard import Key, Controller
import time
import pyperclip

code_list=["837809.OC","832954.OC","831518.OC","835037.OC","831672.OC","836957.OC","430120.OC","870381.OC","839680.OC","836024.OC","831641.OC","872905.OC","833429.OC","430222.OC","833637.OC","834044.OC","836366.OC","872123.OC","832585.OC","872222.OC","831080.OC","871346.OC","832554.OC","831866.OC","871234.OC","872230.OC","834019.OC","831378.OC","835900.OC","835995.OC","835513.OC","870804.OC","430369.OC","832305.OC","832651.OC","836312.OC","833427.OC","834933.OC","839181.OC","873253.OC","831057.OC","871664.OC","833455.OC","834720.OC","872987.OC","835666.OC","834483.OC","831916.OC","835852.OC","872868.OC","832347.OC","832422.OC","873158.OC","836941.OC","832063.OC","830779.OC","838171.OC","871706.OC","833548.OC","837157.OC","831053.OC","833453.OC","838244.OC","873437.OC","839826.OC","835401.OC","430588.OC","870019.OC","836442.OC","870840.OC","833260.OC","834102.OC","870126.OC","834902.OC","831702.OC","837865.OC","430497.OC","836521.OC","870583.OC","834026.OC","839194.OC","837663.OC","830813.OC","830988.OC","430706.OC","430632.OC","831591.OC","839790.OC","839461.OC","835721.OC","430504.OC","839724.OC","839874.OC","839182.OC","837602.OC","834037.OC","837592.OC","831193.OC","833505.OC","430405.OC","870168.OC","835990.OC","832119.OC","837092.OC","871660.OC","831271.OC","836306.OC","872438.OC","839655.OC","871510.OC","831438.OC","839715.OC","835501.OC","831793.OC","833523.OC","838949.OC"]

input_pos=(105, 115)
download_pos=(1454, 165)
terminal_pos=(335, 971)
i=0
for code in code_list:
    i+=1
    if i <32:
        continue
    print(code)
    pyperclip.copy(code)

    mouse.Controller().position=input_pos
    mouse.Controller().click(mouse.Button.left) # 点击输入框
    time.sleep(0.5)
    mouse.Controller().click(mouse.Button.left) # 点击输入框

    keyboard = Controller()
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        time.sleep(0.01)
        keyboard.release('v')
    time.sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)

    mouse.Controller().position=terminal_pos
    mouse.Controller().click(mouse.Button.left) # 点击终端框，以便确认下载完毕
    input('right stock?')
    mouse.Controller().position=download_pos
    mouse.Controller().click(mouse.Button.left) # 点击下载
    print('clicked!')
    mouse.Controller().position=terminal_pos
    mouse.Controller().click(mouse.Button.left) # 点击终端框，以便确认下载完毕
    input('finish？')

