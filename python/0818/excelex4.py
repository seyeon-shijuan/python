'''
Created on 2020. 8. 18.
@author: GDJ24
excelex4.py : xls 파일을 읽고 쓰기
'''

from xlrd import open_workbook
from xlwt import Workbook #pip install xlwt

infile = "ssec1804.xls"
outfile = "ssec1804out.xls"

outworkbook = Workbook()  #비어있는 xls 파일 생성
out_sheet = outworkbook.add_sheet("전체 증감") #sheet 추가

#workbook : infile의 내용을 저장 xls 파일 전체
with open_workbook(infile) as workbook :
    #worksheet : sheet 이름이 "1.전체증감"인 데이터를 저장
    worksheet = workbook.sheet_by_name("1.전체증감")
    for rindex in range(worksheet.nrows) :
        for cindex in range(worksheet.ncols) :
            out_sheet.write(rindex,cindex,worksheet.cell_value(rindex,cindex))
            print(rindex,"x",cindex,worksheet.cell_value(rindex,cindex))
            '''
            예시
            1 x 0 1. 전체 경제활동인구 총괄 증감
            ...
            56 x 4 -6.0
            56 x 5 134.0
            56 x 6 -0.10000000000000142
            56 x 7 -0.10000000000000142
            56 x 8 -0.10000000000000053
            '''
outworkbook.save(outfile) #파일로 저장해서 내보내는 커맨드