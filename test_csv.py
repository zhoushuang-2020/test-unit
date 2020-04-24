#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import csv
import os
from xlrd import open_workbook

#获取当前目录的路径
path=os.path.abspath('.')
csv_path=r'D:\login.csv'
print(path)
csv_file=csv.reader(open(csv_path,'r'))
print(csv_file)
content=[]

for line in csv_file:
    print(line)
    content.append(line)
print('数据：',content)

excel_path='D:\\1.xlsx'
file=open_workbook(excel_path)
sheet = file.sheet_by_name('Sheet1')
nrows=sheet.nrows #总行数
ncols=sheet.ncols #总列数
print("nrows:",nrows,'\n','ncols:',ncols)
#print(sheet.row_values(0)[0])      #打印第一行  第一列
table=file.sheets()[0]
for i in range(0,nrows):
    rowvaule= sheet.row_values(i)
    for data in rowvaule:
        print(data,' ')
    
