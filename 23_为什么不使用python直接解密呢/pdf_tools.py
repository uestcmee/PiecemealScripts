# -*- coding: utf-8 -*-
# 无法打包exe，tkdnd无法导入
from tkinter import *
from tkinter.messagebox import showerror
import os, re
import windnd
from decrypt import decrypt_pdf


# 将拖入的文件添加到listbox中
def drop(files):
    file_list=files

    for file in file_list:
        file=file.decode('gbk')
        print(file)
        if str(file)[-4:]!='.pdf':
            result.insert(END, file + '非PDF文件，添加失败\n')
            continue
        elif ' ' in file:
            result.insert(END, file +'名称含空格，已改名\n')
            os.rename(file,file.replace(' ','_'))
            file=file.replace(' ','_')
        result.insert(END, file + '添加成功\n')
        lb.insert("end", file)


# 打开选中的文件
def open_file():
    result.delete(1.0,END)
    file_names=[lb.get(i) for i in range(lb.size())] # 列表中的文件名
    if len(file_names)==0:
        result.insert(END, '无文件，请添加文件\n')
    for file_name in file_names:

        print (file_name)
        file_name=file_name.replace('\\','/')
        file=file_name.split('/')[-1]
        path=file_name.replace(file,'')#.encode('utf-8')
        file=file#.encode('utf-8')

        decrypt_pdf(file,'')
        result.insert(END, file_name+'解密完成\n')

if __name__ == '__main__':
    root = Tk()

    root.title("PDF解密小工具（仅针对可打开不可复制类的）")
    root.geometry('600x350+00+200')  # 位置设置

    dnd=windnd.hook_dropfiles(root,func=drop)
    # lb = Listbox(root, height=7, width=60, selectmode=SINGLE)
    lb = Listbox(root, height=7, width=60)#, selectmode=MULTIPLE)
    result = Text(root, width=60, height=9)  # 处理结果展示


    button=Button(root, text="开始转换", width=10, command=open_file)
    Label(root,text='拖动文件到此：').grid(row=0,column=0)
    Label(root,text='信息输出：').grid(row=7,column=0)

    lb.grid(row=0, rowspan=5, column=1, columnspan=5, padx=20)
    button.grid(row=6, column=5, padx=10, ipadx=10, pady=10)
    result.grid(row=7, rowspan=5, column=1, columnspan=5, padx=20)

    root.mainloop()