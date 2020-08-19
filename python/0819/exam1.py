'''
Created on 2020. 8. 19.
@author: GDJ24
exam1.py : sales_2015.xlsx 파일 중 sheet = january_2015에서 Customer Name 컬럼 값이 J로 시작하는 행만 선택하여 Sales_2015_J.xlsx 파일로 생성하기
'''

import pandas as pd

infile = "sales_2015.xlsx"
outfile = "Sales_2015_J.xlsx"
df = pd.read_excel(infile, sheet_name="january_2015", index_col=None)
df_value = df[df['Customer Name'].str.startswith("J")]
writer = pd.ExcelWriter(outfile, engine="openpyxl")
df_value.to_excel(writer,sheet_name="sale_2015",index=False)
writer.save()
print("done")

#excelex6에서 for구문 쓴거는 sheet가 여러개인데
#여기에서는 sheet 1개만 할거라서 필요 없음.
#for worksheet_name,data in df.items() : > worksheet_name이 시트고, data가 실제 데이터임