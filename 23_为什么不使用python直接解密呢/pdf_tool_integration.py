# -*- coding: utf-8 -*-
# 使用PyPDF解密
from tkinter import *
import os
import windnd
from PyPDF3 import PdfFileReader
from PyPDF3 import PdfFileWriter
import traceback
import os.path



def write_result(str1,str2):
    global result,result2
    result.insert(END, str1+ '\n')
    result2.insert(END, str2 + '\n')

# 读取文件
def get_reader(filename, password):
    global old_file
    try:
        old_file = open(filename, 'rb')
    except Exception as err:
        print('文件打开失败！' + str(err))
        write_result(filename,'文件打开失败')
        return None

    # 创建读实例

    pdf_reader = PdfFileReader(old_file, strict=False)
    # 解密操作
    if pdf_reader.isEncrypted:
        if password is None:
            print('%s文件被加密，需要密码！' % filename)
            write_result(filename, '文件需要密码')
            return None
        else:
            if pdf_reader.decrypt(password) != 1:
                print('%s密码不正确！' % filename)
                return None
    # if 'old_file' in locals(): # 这句话需要使用字符串格式，否则无法关闭文件
    #     old_file.close()
    return pdf_reader


# 进行解密
def decrypt_pdf(filename, password, decrypted_filename=None):
    global old_file
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
        write_result(filename, '文件打开失败')
        return '出错'
    if not pdf_reader.isEncrypted:
        print('文件没有被加密，无需操作！')
        return '未加密，无需操作！'
    pdf_writer = PdfFileWriter()
    pdf_writer.appendPagesFromReader(pdf_reader)
    # decrypted_filename=filename
    if decrypted_filename is None:
        decrypted_filename =  "".join(filename[:-4])+'_'+ 'decrypted' + '.pdf'
    # 写入新文件
    pdf_writer.write(open(decrypted_filename, 'wb'))
    file_name = re.split('\\\|/',filename)[-1]

    old_file.close()

    try:
        os.remove(filename)
        os.rename(decrypted_filename,filename)
        write_result(file_name, '已覆盖旧文件')
    except:
        traceback.print_exc()
        write_result(file_name,'删除旧文件失败')

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
            result2.insert(END,'非PDF文件'+'\n')
            result.insert(END, file_name+ '\n')
            continue
        elif ' ' in file:
            result2.insert(END,'含空格，已改名'+'\n')
            result.insert(END, file_name+'\n')
            os.rename(file,file.replace(' ','_'))
            file=file.replace(' ','_')
        if file in file_names:
            result2.insert(END,'已存在'+'\n')
            result.insert(END, file_name + '\n')
            continue
        result2.insert(END,'添加成功'+'\n')
        result.insert(END, file_name+ '\n')
        lb.insert("end", file)


# 打开选中的文件
def open_file():
    result.delete(0,END)
    result2.delete(0, END)
    file_names=list(set([lb.get(i) for i in range(lb.size())])) # 列表中的文件名，去重
    if len(file_names)==0:
        result.insert(END, '无文件，请添加文件\n')
    for file_name in file_names:
        print (file_name)
        file_name=file_name.replace('\\','/')
        file=file_name.split('/')[-1]

        # result2.insert(END,'开始解密'+'\n')
        # result.insert(END, file+'\n')

        # 解密函数
        try:
            words=decrypt_pdf(file_name,'')
        except:
            words='解密失败'
            pass

        result2.insert(END,words+'\n')
        result.insert(END, file+'\n')
    lb.delete(0, END) # 清空上文中的待解密文件


# 清空内容
def clear():
    result.delete(0, END)
    result2.delete(0, END)
    lb.delete(0,END)


if __name__ == '__main__':
    root = Tk()
    # 名称和位置
    root.title("PDF解密小工具")
    root.iconbitmap('panda.ico')  # 更改窗口图标

    #root.geometry('800x350+00+200')  # 位置设置
    root.resizable(0, 0)  # 设置窗口大小不可变
    dnd=windnd.hook_dropfiles(root,func=drop)
    lb = Listbox(root, height=7, width=80)
    result = Listbox(root, width=60, height=9)  # 处理结果展示
    result2 = Listbox(root, width=15, height=9)  # 处理结果展示

    button=Button(root, text="开始转换", width=10, command=open_file)
    Button(root, text="清空内容", width=10, command=clear).grid(row=6,column=4)
    Label(root,text='拖动文件到此：').grid(row=0,column=0)
    Label(root,text='信息输出：').grid(row=7,column=0)
    Label(root,text='').grid(row=12,column=0)

    # 调整位置
    lb.grid(row=0, rowspan=5, column=1, columnspan=5, padx=20)
    button.grid(row=6, column=5, padx=10, ipadx=10, pady=10)
    result.grid(row=7, rowspan=5, column=1, columnspan=4, padx=20,sticky=E)
    result2.grid(row=7, rowspan=5, column=5, columnspan=1, padx=20,sticky=W)

    root.mainloop()