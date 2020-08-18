'''
Created on 2020. 8. 18.
@author: GDJ24
excelex2.py : xlsx의 모든 sheet 읽기
'''

import openpyxl
filename = "sales_2015.xlsx"
book = openpyxl.load_workbook(filename)
#book.worksheets : sheet의 리스트
for sheet in book.worksheets :
    data=[]
    #sheet.rows : sheet의 행을 의미한다. row는 한 줄을 의미
    for row in sheet.rows :
        line=[]
        for i,c in enumerate(row) :
            line.append(c.value)
        print(line)
        data.append(line)
        
