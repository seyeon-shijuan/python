'''
Created on 2020. 8. 14.
@author: GDJ24
pandasex5.py : column 선택하기
iloc : index를 기준으로 조회
loc : 이름 기준으로 조회
'''

import pandas as pd
infile = "supplier_data.csv"
df = pd.read_csv(infile)
df_col = df.iloc[:,[0,3]] #[row,column] : 모든 row, 0,1,2 column만 소팅
# : 는 의미하는게 *:*임 전체다 : 전체다 인거를 생략한거임 :가 전체를 의미하는게 아니라
#아래에 다음 예시 있음
print("df.iloc[:,[0,3]]=>")
print(df_col)

'''
df.iloc[:,[0,3]]=>
   Supplier Name     Cost
0     Supplier X  $500.00
1     Supplier X  $500.00
2     Supplier X  $750.00
3     Supplier X  $750.00
4     Supplier Y  $250.00
5     Supplier Y  $250.00
6     Supplier Y  $125.00
7     Supplier Y  $125.00
8     Supplier Z  $615.00
9     Supplier Z  $615.00
10    Supplier Z  $615.00
11    Supplier Z  $615.00
'''

print("행: 0~3개의 행, 열: 0~2개의 열을 조회해보자")
df_col = df.iloc[0:4,0:3]
print(df_col)
'''
행: 0~3개의 행, 열: 0~2개의 열을 조회해보자
  Supplier Name Invoice Number  Part Number
0    Supplier X       001-1001         2341
1    Supplier X       001-1001         2341
2    Supplier X       001-1001         5467
3    Supplier X       001-1001         5467
'''

print("#모든 행의 Invoice Number, Cost 컬럼 조회하기")
df_col = df.loc[:,["Invoice Number","Cost"]]
print(df_col)

'''
#모든 행의 Invoice Number, Cost 컬럼 조회하기
   Invoice Number     Cost
0        001-1001  $500.00
1        001-1001  $500.00
2        001-1001  $750.00
3        001-1001  $750.00
4         50-9501  $250.00
5         50-9501  $250.00
6         50-9505  $125.00
7         50-9505  $125.00
8        920-4803  $615.00
9        920-4804  $615.00
10       920-4805  $615.00
11       920-4806  $615.00
'''

print("#Invoice Number 값이 920- 으로 시작하는 행의 Invoice Number와 Cost 컬럼을 조회하자")
#앞에는 row의 조건, 뒤는 column 조건
df_col = df.loc[df["Invoice Number"].str.startswith("920-"),["Invoice Number","Cost"]]
print(df_col)
'''
#Invoice Number 값이 920- 으로 시작하는 행의 Invoice Number와 Cost 컬럼을 조회하자
   Invoice Number     Cost
8        920-4803  $615.00
9        920-4804  $615.00
10       920-4805  $615.00
11       920-4806  $615.00
'''
