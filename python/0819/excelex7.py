'''
Created on 2020. 8. 19.
@author: GDJ24
excelex7.py : pandas를 이용하여 xls 파일 읽기
출력되는 excel 파일의 sheet를 여러개로 저장ㅎ기
'''

import pandas as pd
infile = "../0818/ssec1804.xls"
outfile = "ssec1804_bak.xls"
writer = pd.ExcelWriter(outfile)
df = pd.read_excel(infile, sheet_name=None, index_col=None)
for worksheet_name, data in df.items() :
    data.to_excel(writer,sheet_name=worksheet_name, index=False,header=False)
    #sheet 별로 excel 파일에 저장
writer.save()
print('done')