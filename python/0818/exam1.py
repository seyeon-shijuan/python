'''
Created on 2020. 8. 18.
@author: GDJ24
exam1.py : ssec1804.xls 파일에서 1.남자, 1.여자 sheet의 내용을 ssec1804mf.xls 파일에 남자, 여자 sheet로 저장하기
'''

from xlrd import open_workbook
from xlwt import Workbook

def makesheet(output_sheet):
    for row_index in range(worksheet.nrows) :
        for column_index in range(worksheet.ncols) :
            output_sheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))
        #print(worksheet.cell_value(row_index, column_index))
    #print("Done")

infile="ssec1804.xls"
outfile="ssec1804mf.xls"

worksheet = None
outworkbook = Workbook()
out_sheet1 = outworkbook.add_sheet("남자")
out_sheet2 = outworkbook.add_sheet("여자")


#with 문장을 쓰면  __enter__()랑 __exit__()가 처음과 끝에 call된다.
#for clause 대신 쓴다고 생각하면 되는데, for의 경우에 .close() 이 method를 마지막에 해줘야된다.
with open_workbook(infile) as workbook :
    worksheet = workbook.sheet_by_name("1.남자")
    makesheet(out_sheet1)
    worksheet = workbook.sheet_by_name("1.여자")
    makesheet(out_sheet2)
            
outworkbook.save(outfile)

