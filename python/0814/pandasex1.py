'''
Created on 2020. 8. 14.
@author: GDJ24
pandasex1.py : pandas 예제
'''

import pandas as pd #pip install pandas
df = pd.DataFrame({"A":[1,4,7],"B":[2,5,8],"C":[3,6,9]})
print(type(df)) #<class 'pandas.core.frame.DataFrame'>
print(df)
'''
행선택
iloc : 순서, 인덱스 기준
loc : 이름기준
'''

print("인덱스 값 조회하기")
print(df.iloc[0])
print(df.iloc[1])
print(df.loc[0])
#print(df.ix[0])  #버전 2에만 있음..

#열선택
print("A 열 =")
print(df["A"])


'''
<class 'pandas.core.frame.DataFrame'>
   A  B  C
0  1  2  3
1  4  5  6
2  7  8  9
인덱스 값 조회하기
A    1
B    2
C    3
Name: 0, dtype: int64
A    4
B    5
C    6
Name: 1, dtype: int64
A    1
B    2
C    3
Name: 0, dtype: int64
A 열 =
0    1
1    4
2    7
Name: A, dtype: int64
'''

print("♥")
df = pd.DataFrame(data=([[1,2,3],[4,5,6],[7,8,9]]),index=[2,"A",4],columns=[51,52,54])
print(df)
'''
   51  52  54
2   1   2   3
A   4   5   6
4   7   8   9
'''
print(df[51],"★") #Name: 51, dtype: int64 ★

print("df.ilic[2]=>")
print(df.iloc[2])
print("df.lic[2]=>")
print(df.loc[2]) 
'''df.ilic[2]=>
51    7
52    8
54    9
Name: 4, dtype: int64
df.lic[2]=>
51    1
52    2
54    3
Name: 2, dtype: int64
'''
