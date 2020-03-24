import pynput.mouse as mouse
import time
import pyperclip

mouse.Controller().click(mouse.Button.left,1)


def record_mouse():
    while True:
        pos=mouse.Controller().position
        print(pos)
        time.sleep(1)
record_mouse()