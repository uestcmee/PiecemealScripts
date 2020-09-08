import pyperclip,time,datetime

raw_text = pyperclip.paste()
pyperclip.copy('aaa\na aa\nbb')
while True:
    raw_text=pyperclip.paste()
    # print(raw_text)
    text = raw_text.replace('\t','').replace(' ','').replace('\n','').replace('\r','')
    # print(pyperclip.paste())
    if raw_text==text:
        time.sleep(1)
        continue
    print(datetime.datetime.now(),text)
    # print(raw_text,text)
    pyperclip.copy(text)
    time.sleep(1)
