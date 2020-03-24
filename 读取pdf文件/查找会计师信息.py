
import os
import pdfplumber
import pandas as pd
import sys
pdf_dir='C:\\Wind\Wind.NET.Client\\WindNET\\users\\W47779091884\\NA'

def get_pdf_name(pdf_dir):

    files=os.listdir(pdf_dir)
    pdfs=[]
    for file in files:
        if file[-3:]=='pdf': # 找到文件夹中的pdf文件
            pdfs.append(file)
    return pdfs


def get_account(pdf_name):
    with pdfplumber.open(pdf_name) as pdf:
        # 对应表格出现的大致页数
        for page in range(6, 15):
            page_content = pdf.pages[page]
            # 循环查找寻找到的表格
            for table in page_content.extract_tables():
                if table[0][0] == '主办券商': # 找到所需的表格
                    df = pd.DataFrame(table)
                    # 第一列当成表头： df = pd.DataFrame(table[1:],columns=table[0])
                    account_agency = df.iloc[3][1] # 获取事务所名称给
                    accountant = df.iloc[4][1] # 获取会计师名称
                    return account_agency, accountant
        return 0,0


pdfs=get_pdf_name(pdf_dir)

# 初始化字典
account_dic = {}

for pdf_name in pdfs: # 循环文件夹中的pdf文件
    print(pdf_name)
    code=pdf_name.split('-')[3]  # 股票代码


    # 获取事务所和会计信息
    agency,accountant=get_account(pdf_dir + '\\' + pdf_name)
    print(agency,accountant)
    account_dic[code]=[agency,accountant]
    # print(account_dic)
df=pd.DataFrame(account_dic)
df=df.T
print(df)
df.to_csv('account.csv')



