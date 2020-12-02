# -*- coding: utf-8 -*-
# 无法打包exe，tkdnd无法导入
from tkinter import *
from tkinter.messagebox import showerror
import os, re


# 加载tkdnd
class TkDnD:
    def __init__(self, tkroot):
        self._tkroot = tkroot
        tkroot.tk.eval('package require tkdnd')
        # make self an attribute of the parent window for easy access in child classes
        tkroot.dnd = self

    def bindsource(self, widget, type=None, command=None, arguments=None, priority=None):
        '''Register widget as drag source; for details on type, command and arguments, see bindtarget().
        priority can be a value between 1 and 100, where 100 is the highest available priority (default: 50).
        If command is omitted, return the current binding for type; if both type and command are omitted,
        return a list of registered types for widget.'''
        command = self._generate_callback(command, arguments)
        tkcmd = self._generate_tkcommand('bindsource', widget, type, command, priority)
        res = self._tkroot.tk.eval(tkcmd)
        if type == None:
            res = res.split()
        return res

    def bindtarget(self, widget, type=None, sequence=None, command=None, arguments=None, priority=None):
        '''Register widget as drop target; type may be one of text/plain, text/uri-list, text/plain;charset=UTF-8
        (see the man page tkDND for details on other (platform specific) types);
        sequence may be one of '<Drag>', '<DragEnter>', '<DragLeave>', '<Drop>' or '<Ask>' ;
        command is the callback associated with the specified event, argument is an optional tuple of arguments
        that will be passed to the callback; possible arguments include: %A %a %b %C %c %D %d %L %m %T %t %W %X %x %Y %y
        (see the tkDND man page for details); priority may be a value in the range 1 to 100 ; if there are
        bindings for different types, the one with the priority value will be proceeded first (default: 50).
        If command is omitted, return the current binding for type, where sequence defaults to '<Drop>'.
        If both type and command are omitted, return a list of registered types for widget.'''
        command = self._generate_callback(command, arguments)
        tkcmd = self._generate_tkcommand('bindtarget', widget, type, sequence, command, priority)
        res = self._tkroot.tk.eval(tkcmd)
        if type == None:
            res = res.split()
        return res

    def clearsource(self, widget):
        '''Unregister widget as drag source.'''
        self._tkroot.tk.call('dnd', 'clearsource', widget)

    def cleartarget(self, widget):
        '''Unregister widget as drop target.'''
        self._tkroot.tk.call('dnd', 'cleartarget', widget)

    def drag(self, widget, actions=None, descriptions=None, cursorwindow=None, command=None, arguments=None):
        '''Initiate a drag operation with source widget.'''
        command = self._generate_callback(command, arguments)
        if actions:
            if actions[1:]:
                actions = '-actions {%s}' % ' '.join(actions)
            else:
                actions = '-actions %s' % actions[0]
        if descriptions:
            descriptions = ['{%s}' % i for i in descriptions]
            descriptions = '{%s}' % ' '.join(descriptions)
        if cursorwindow:
            cursorwindow = '-cursorwindow %s' % cursorwindow
        tkcmd = self._generate_tkcommand('drag', widget, actions, descriptions, cursorwindow, command)
        self._tkroot.tk.eval(tkcmd)

    def _generate_callback(self, command, arguments):
        '''Register command as tk callback with an optional list of arguments.'''
        cmd = None
        if command:
            cmd = self._tkroot._register(command)
            if arguments:
                cmd = '{%s %s}' % (cmd, ' '.join(arguments))
        return cmd

    def _generate_tkcommand(self, base, widget, *opts):
        '''Create the command string that will be passed to tk.'''
        tkcmd = 'dnd %s %s' % (base, widget)
        for i in opts:
            if i is not None:
                tkcmd += ' %s' % i
        return tkcmd


# 将拖入的文件添加到listbox中
def drop(files):
    # print(files)
    # 拖入文件有特殊符号解决
    if isinstance(files, str): # 判断输入为str格式
        # s = re.compile(r'[{](.*?)[}]').findall(files) # 特殊符号{}过滤

        file_list = re.sub(u"{.*?}", "", files).split()  # 通过空格切分多文件，所以文件名中不能有空格
        error_list=re.findall(u"{(.*?)}",files)
        if error_list:
            print('以下文件名称中含有空格，添加失败')
            for one in error_list:
                if ' ' in one: #or '-' in one:
                    result.insert(END, one +'名称含空格，已改名\n')
                    os.rename(one,one.replace(' ','_'))
                    file_list.append(one.replace(' ','_'))
                else:
                    file_list.append(one)

    else:
        return 0
    for file in file_list:
        print(file)
        if str(file)[-4:]!='.pdf':
            result.insert(END, file + '非PDF文件，添加失败\n')
            continue
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
        order=u'qpdf.exe --decrypt {} {}解密_{}'.format(file_name,path,file)
        print(order)
        os.system(order)
        result.insert(END, file_name+'解密完成\n')



if __name__ == '__main__':
    root = Tk()

    root.title("PDF解密小工具（仅针对可打开不可复制类的）")
    root.geometry('600x350+00+200')  # 位置设置
    # root.wm_resizable(False, False)  # 不允许修改长宽
    dnd = TkDnD(root)
    # lb = Listbox(root, height=7, width=60, selectmode=SINGLE)
    lb = Listbox(root, height=7, width=60)#, selectmode=MULTIPLE)
    result = Text(root, width=60, height=9)  # 处理结果展示
    dnd.bindtarget(lb, 'text/uri-list', '<Drop>', drop, ('%D',))
    # 这两个是将文件拖入框内时绑定的事件，可以自己写函数测试
    # dnd.bindtarget(lb, 'text/uri-list', '<Drag>', lambda x:x, ('%A', ))
    # dnd.bindtarget(lb, 'text/uri-list', '<DragEnter>', drag, ('%A', ))

    button=Button(root, text="开始转换", width=10, command=open_file)
    Label(root,text='拖动文件到此：').grid(row=0,column=0)
    Label(root,text='信息输出：').grid(row=7,column=0)

    lb.grid(row=0, rowspan=5, column=1, columnspan=5, padx=20)
    button.grid(row=6, column=5, padx=10, ipadx=10, pady=10)
    result.grid(row=7, rowspan=5, column=1, columnspan=5, padx=20)

    root.mainloop()