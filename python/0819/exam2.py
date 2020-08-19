'''
Created on 2020. 8. 19.
@author: GDJ24
exam2.py : sales_2013.xlsx 파일 중 Purchase Date 컬럼의 값이 "01/24/2013"과 "01/31/2013"인 행만 sales_2013_01.xlsx 파일로 저장하기
isin 함수 사용
'''

import pandas as pd

infile="sales_2013.xlsx"
outfile="sales_2013_01.xlsx"
#df : sales_2013.xlsx 파일의 모든 시트의 데이터를 pandas의 dataframe 타입으로 저장
df=pd.read_excel(infile, sheet_name=None, index_col=None)
row_output=[]
for worksheet_name, data in df.items() :
    #data중 컬럼의 이름이 Purchase Date인 값중에 isin안에 속한 값만 선택해서 row_output에 append 된다.
    row_output.append(data[data["Purchase Date"].isin(['01/24/2013','01/31/2013'])])
filtered_row = pd.concat(row_output, axis=0, ignore_index=True)
writer = pd.ExcelWriter(outfile,engine="openpyxl")
filtered_row.to_excel(writer,sheet_name="sale_2013",index=False)
writer.save()
print('done')