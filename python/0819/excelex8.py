'''
Created on 2020. 8. 19.
@author: GDJ24
excelex8.py : 폴더에 속한 excel 파일을 선택
'''

import pandas as pd
import glob
import os # 시스템 관련된 모듈
inpath="D:/Python/python/excel"
outfile="sales_all.xlsx"
#"*.xlsx" : inpath 안에있는 모든 xlsx 파일을 선택한다.
excels = glob.glob(os.path.join(inpath,"*.xlsx"))
rows=[] #DataFrame 객체를 list로 저장하는 객체
for excel in excels :
    print(excel)
    dfs = pd.read_excel(excel, sheet_name=None, index_col=None)
    for sheet_name, df in dfs.items() :
        rows.append(df)
#excel 파일로 저장
#axis=0 : row로 추가
#df_concat  : 지정된 폴더에 있는 엑셀파일의 모든 sheet의 데이터를 저장
#row 형태로 추가됨
df_concat = pd.concat(rows, sort=False, axis=0,ignore_index=True)
writer =pd.ExcelWriter(outfile) 
df_concat.to_excel(writer,sheet_name="all_data_all_worksheet",index=False)
writer.save()

