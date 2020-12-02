# coding:utf-8
import os
from PyPDF3 import PdfFileReader
from PyPDF3 import PdfFileWriter


def get_reader(filename, password):
    try:
        old_file = open(filename, 'rb')
        # print('run  jiemi1')
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
    # print('run  jiemi')
    pdf_reader = get_reader(filename, password)
    if pdf_reader is None:
        return
    if not pdf_reader.isEncrypted:
        print('文件没有被加密，无需操作！')
        return
    pdf_writer = PdfFileWriter()

    pdf_writer.appendPagesFromReader(pdf_reader)

    if decrypted_filename is None:
        decrypted_filename =  'decrypted'+ '_' +"".join(filename[:-4])  + '.pdf'

    # 写入新文件
    pdf_writer.write(open(decrypted_filename, 'wb'))
    print('解密完成，新文件存储至'+decrypted_filename)


if __name__ == '__main__':
    decrypt_pdf('加密的.pdf', '')  # 密码不知道，就设置为空