#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import xlrd
import os

class read_Excel():
    def read_excel(xls_name,sheet_name):
        cls=[]
        #获取excel路径
        xlspath=os.path.join('D:\\',xls_name)
        file=xlrd.open_workbook(xlspath)

        sheet = file.sheet_by_name(sheet_name)#获取excel的sheet

        nrows = sheet.nrows#行数
        ncols = sheet.ncols
        keys=sheet.row_values(0)
        #print('keys:',keys)
        cell=sheet.cell_value(0,0) #第一行第一列
        #print('cell:',cell)
        for i in range(nrows):
            a=sheet.row_values(i)

            cls.append(a)
        return cls

if __name__=='__main__':
    print(read_Excel.read_excel('1.xlsx','Sheet1'))
    print('用户名：',read_Excel.read_excel('1.xlsx', 'Sheet1')[1][0])
    print('密码：', read_Excel.read_excel('1.xlsx', 'Sheet1')[1][1])

