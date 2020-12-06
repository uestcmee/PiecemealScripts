# -*- coding: utf-8 -*-
# 使用PyPDF解密
from tkinter import *
import os
import windnd
from PyPDF3 import PdfFileReader
from PyPDF3 import PdfFileWriter


def get_reader(filename, password):
    try:
        old_file = open(filename, 'rb')
    except Exception as err:
        print('文件打开失败！' + str(err))
        return None

    # 创建读实例
    pdf_reader = PdfFileReader(old_file, strict=False)

    # 解密操作
    if pdf_reader.isEncrypted:
        if password is None:
            print('%s文件被加密，需要密码！' % filename)
            return None
        else:
            if pdf_reader.decrypt(password) != 1:
                print('%s密码不正确！' % filename)
                return None
    if old_file in locals():
        old_file.close()
    return pdf_reader


def decrypt_pdf(filename, password, decrypted_filename=None):
    """
    将加密的文件及逆行解密，并生成一个无需密码pdf文件
    :param filename: 原先加密的pdf文件
    :param password: 对应的密码
    :param decrypted_filename: 解密之后的文件名
    :return:
    """
    # 生成一个Reader和Writer
    pdf_reader = get_reader(filename, password)
    if pdf_reader is None:
        return '出错'
    if not pdf_reader.isEncrypted:
        print('文件没有被加密，无需操作！')
        return '文件没有被加密，无需操作！'
    pdf_writer = PdfFileWriter()
    pdf_writer.appendPagesFromReader(pdf_reader)
    if decrypted_filename is None:
        decrypted_filename =  "".join(filename[:-4])+'_'+ 'decrypted' + '.pdf'
    # 写入新文件
    pdf_writer.write(open(decrypted_filename, 'wb'))
    print('解密完成，新文件存储至'+decrypted_filename)
    return '解密完成'


# 将拖入的文件添加到listbox中
def drop(files):
    file_list=files
    file_names = list(set([lb.get(i) for i in range(lb.size())]))  # 列表中的文件名
    for file in file_list:
        file=file.decode('gbk')
        file_name=file.split('\\')[-1]

        print(file)
        if str(file)[-4:]!='.pdf':
            result.insert(END, file_name+'..'*(60-len(file_name)) + '非PDF文件\n')
            continue
        elif ' ' in file:
            result.insert(END, file_name+'..'*(60-len(file_name)) +'名称含空格，将改名\n')
            os.rename(file,file.replace(' ','_'))
            file=file.replace(' ','_')
        if file in file_names:
            result.insert(END, file_name +'..'*(60-len(file_name))+ '已存在，添加失败\n')
            continue
        result.insert(END, file_name+'..'*(60-len(file_name)) + '添加成功\n')
        lb.insert("end", file)


# 打开选中的文件
def open_file():
    result.delete(0,END)
    file_names=list(set([lb.get(i) for i in range(lb.size())])) # 列表中的文件名，去重
    if len(file_names)==0:
        result.insert(END, '无文件，请添加文件\n')
    for file_name in file_names:
        print (file_name)
        file_name=file_name.replace('\\','/')
        file=file_name.split('/')[-1]
        result.insert(END, file+'..'*(60-len(file_name))+'开始解密'+'\n')

        words=decrypt_pdf(file_name,'')
        result.insert(END, file+'..'*(60-len(file_name))+words+'\n')


def clear():
    result.delete(0, END)
    lb.delete(0,END)


if __name__ == '__main__':
    root = Tk()
    # 名称和位置
    root.title("PDF解密小工具")
    root.geometry('800x350+00+200')  # 位置设置

    dnd=windnd.hook_dropfiles(root,func=drop)
    lb = Listbox(root, height=7, width=80)
    result = Listbox(root, width=80, height=9)  # 处理结果展示

    button=Button(root, text="开始转换", width=10, command=open_file)
    Button(root, text="清空内容", width=10, command=clear).grid(row=6,column=4)
    Label(root,text='拖动文件到此：').grid(row=0,column=0)
    Label(root,text='信息输出：').grid(row=7,column=0)
    # 调整位置
    lb.grid(row=0, rowspan=5, column=1, columnspan=5, padx=20)
    button.grid(row=6, column=5, padx=10, ipadx=10, pady=10)
    result.grid(row=7, rowspan=5, column=1, columnspan=5, padx=20)

    root.mainloop()