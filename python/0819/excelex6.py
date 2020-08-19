'''
Created on 2020. 8. 19.
@author: GDJ24
excelex6.py : pandas를 이용한 xlsx 파일 읽기
1. xlsx 파일의 모든 sheet 데이터 읽기
2. 생성되는 excel 파일로 하나의 sheet로 데이터를 저장한다.
    조건에 맞는 경우로 소팅할 수 있다.
'''

import pandas as pd

infile = "sales_2015.xlsx"
outfile = "sales_all.xlsx"
df = pd.read_excel(infile, sheet_name=None, index_col=None)
row_output = []
#df.items() : sheet 정보
#sheet 이름, sheet 데이터 
for worksheet_name,data in df.items() :
    print("===",worksheet_name, "===") # === january_2015 ===
    row_output.append(data[data["Sale Amount"].replace("$",'').replace(",",'').astype(float) > 200.0])
    #raw data에 Sale Amount의 값은 $234,436.00 형태로 되어있어서 replace()로 $랑 ,를 물리적으로 없앤다. 그리고 float 기준으로 200보다큰 경우만 필터링한다. 
    #조건에 맞으면 줄 자체가 row_output list에 append 된다.
    #axis=0이면 아래로 추가, axis=1이면 오른쪽으로 추가 > 당연히 axis는 0이어야 한다.
filtered_row = pd.concat(row_output,axis=0, ignore_index=True)
writer = pd.ExcelWriter(outfile,engine="openpyxl")
#to_excel(작성객체,sheet_name="출력할이름",index=False<-조건인데 기본 False로 한다.)
#그러면 dataframe 타입에서 excel로 바뀌면서 writer 객체에 들어가진다.
filtered_row.to_excel(writer,sheet_name="sale_2015",index=False)
writer.save()



