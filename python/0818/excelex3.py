'''
Created on 2020. 8. 18.
@author: GDJ24
excelex3.py : xls 파일 읽기
'''
from xlrd import open_workbook
infile = "ssec1804.xls"
workbook = open_workbook(infile)
print("sheet의 개수:",workbook.nsheets)
for worksheet in workbook.sheets() :
    print("worksheet 이름 : ",worksheet.name)
    print("행의 개수:",worksheet.nrows)
    print("컬럼의 수:",worksheet.ncols)
    #내용출력
    #row_index : 행의 인덱스
    for row_index in range(worksheet.nrows) :
        #column_index  : 열의 인덱스
        for column_index in range(worksheet.ncols) :
            #worksheet.cell_value(행인덱스,열인덱스) : cell의 값
            print(worksheet.cell_value(row_index,column_index),",",end="")
            print()
            
