'''
Created on 2020. 8. 19.
@author: GDJ24
exam3.py : sales_2013.xlsx 파일이 january_2013 sheet 의 열이 "Customer Name","Sale Amount" 컬럼만 sales_2013_amt.xlsx 파일로 저장하기
'''

import pandas as pd

infile="sales_2013.xlsx"
outfile="sales_2013_amt.xlsx"
df = pd.read_excel(infile, sheet_name='january_2013', index_col=None)
df_value = pd.DataFrame(df, columns = ['Customer Name','Sale Amount'])
writer = pd.ExcelWriter(outfile, engine="openpyxl")
df_value.to_excel(writer,sheet_name="sale_2013",index=False)
writer.save()
print("done")