# 改变excel文件表中的标题
# 删除第四行后的内容
# 无法操作xlsx文件，尴尬
# coding:utf-8
import os
import xlrd
from xlutils.copy import copy


dir='C:\\Users\\zikep\\Desktop\\20200206发改委\\关于做好全国优化营商环境先进经验和典型做法复制\\昆明\\昆明经验总结'
file_names = os.listdir(dir)


def setOutCell(outSheet, col, row, value):
    """ Change cell value without changing formatting. """

    def _getOutCell(outSheet, colIndex, rowIndex):
        """ HACK: Extract the internal xlwt cell representation. """
        row = outSheet._Worksheet__rows.get(rowIndex)
        if not row: return None

        cell = row._Row__cells.get(colIndex)
        return cell

    # HACK to retain cell style.
    previousCell = _getOutCell(outSheet, col, row)
    # END HACK, PART I

    outSheet.write(row, col, value)

    # HACK, PART II
    if previousCell:
        newCell = _getOutCell(outSheet, col, row)
        if newCell:
            newCell.xf_idx = previousCell.xf_idx

for temp in file_names:
    if temp[-4:]=='xlsx':
        continue
    print(temp)
    workbook=xlrd.open_workbook(dir+'\\'+temp,formatting_info=True)
    sheet=workbook.sheet_by_index(0)
    title=sheet.cell_value(1,0)
    print(title)
    new_title=str(title).replace('太原','昆明')
    print(new_title)
    wb=copy(workbook)
    ws=wb.get_sheet(0)

    # 不改变格式的情况下修改标题
    setOutCell(ws,0,1,new_title) # 先列再行

    # 删除第四行之后的部分（通过写入空数据来实现）
    for row in range(3,sheet.nrows):
        for col in range(0,sheet.ncols):
            ws.write(row,col,'')
    wb.save(dir+'\\'+temp)
