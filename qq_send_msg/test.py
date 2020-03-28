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
#监听键盘按键
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()


print('hello')
