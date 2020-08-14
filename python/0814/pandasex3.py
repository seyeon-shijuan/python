'''
Created on 2020. 8. 14.
@author: GDJ24
pandasex3.py
'''

import pandas as pd

infile = "supplier_data.csv"
outfile = "pandas_out3.csv"
df = pd.read_csv(infile)
print(df)

'''
   Supplier Name Invoice Number  Part Number     Cost Purchase Date
0     Supplier X       001-1001         2341  $500.00       1/20/14
1     Supplier X       001-1001         2341  $500.00       1/20/14
2     Supplier X       001-1001         5467  $750.00       1/20/14
3     Supplier X       001-1001         5467  $750.00       1/20/14
4     Supplier Y        50-9501         7009  $250.00       1/30/14
5     Supplier Y        50-9501         7009  $250.00       1/30/14
6     Supplier Y        50-9505         6650  $125.00        2/3/14
7     Supplier Y        50-9505         6650  $125.00        2/3/14
8     Supplier Z       920-4803         3321  $615.00        2/3/14
9     Supplier Z       920-4804         3321  $615.00       2/10/14
10    Supplier Z       920-4805         3321  $615.00       2/17/14
11    Supplier Z       920-4806         3321  $615.00       2/24/14
'''

#14년 1월 20일 -  14년 1월 13일 까지의 데이터만 소팅하기
# isin(importDate),:의 : colon은 모든 컬럼을 의미한다. -> 모든 컬럼에서 comma, 앞의 조건에 해당하는 rows만 부르는 것임.
importDate = ["1/20/14","1/30/14"]
df_inset = df.loc[df["Purchase Date"].isin(importDate),:]
print(df_inset)
'''
  Supplier Name Invoice Number  Part Number     Cost Purchase Date
0    Supplier X       001-1001         2341  $500.00       1/20/14
1    Supplier X       001-1001         2341  $500.00       1/20/14
2    Supplier X       001-1001         5467  $750.00       1/20/14
3    Supplier X       001-1001         5467  $750.00       1/20/14
4    Supplier Y        50-9501         7009  $250.00       1/30/14
5    Supplier Y        50-9501         7009  $250.00       1/30/14
'''
print(type(df_inset)) #<class 'pandas.core.frame.DataFrame'>

#내보내기
#False
df_inset.to_csv(outfile,index=False)

