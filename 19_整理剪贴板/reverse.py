import pyperclip,time,datetime

raw_text = pyperclip.paste()
before_text=0
while True:
    raw_text=pyperclip.paste()
    text = raw_text[::-1] # 换向

    if text==before_text:
        time.sleep(1)
        continue
    print(datetime.datetime.now().strftime('%m-%d %H:%M'),'反转后：',text)
    # print(raw_text,text)
    pyperclip.copy(text)
    before_text=raw_text
    time.sleep(1)
