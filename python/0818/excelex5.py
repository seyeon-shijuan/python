'''
Created on 2020. 8. 18.
@author: GDJ24
excelex5.py : pandas를 이용하여 excel 파일 읽고 쓰기
'''

import pandas as pd
infile = "sales_2015.xlsx"
outfile = "sales_2015_pd.xlsx"
#read_excel(읽을 파일, 시트이름, index_col) : excel file 읽기
df = pd.read_excel(infile,"january_2015",index_col=None)
print(df)
print(type(df)) #<class 'pandas.core.frame.DataFrame'>

df_value = df[df["Sale Amount"].astype(float) >500.0]
#df_value로 조건을 정할 수 있다.

#ExcelWriter(출력파일, 엔진정보=생략가능) : 엔진정보 생략하면 xls가 default임, xlsx로 출력할거면 엔진을 openpyxl로 하면 된다.
writer = pd.ExcelWriter(outfile,engine="openpyxl")
#to_excel(출력객체, 시트네임지정, 인덱스여부) : Pandas의 DataFrame타입인 데이터를 excel 파일로 변경한다.
#df.to_excel(writer,sheet_name="jan_15_out",index=False)
df_value.to_excel(writer,sheet_name="jan_15_out",index=False)
writer.save()


'''
   Customer ID       Customer Name Invoice Number  Sale Amount Purchase Date
0         1234          John Smith       100-0002          123    2015-01-01
1         2345       Mary Harrison       100-0003          543    2015-01-06
2         3456          Lucy Gomez       100-0004          567    2015-01-11
3         4567        Rupert Jones       100-0005          978    2015-01-18
4         5678       Jenny Walters       100-0006          345    2015-01-24
5         6789  Samantha Donaldson       100-0007          645    2015-01-31
<class 'pandas.core.frame.DataFrame'>
'''