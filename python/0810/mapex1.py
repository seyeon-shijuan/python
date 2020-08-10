'''
Created on 2020. 8. 10.
@author: GDJ24
mapex1.py : map = 리스트 각각의 요소를 변경한다.
'''
before = ["2020","08","10"]
print(type(before[0]))
print(before)
after = list(map(int,before))
print(type(after[0]))
print(after)

''''
<class 'str'>
['2020', '08', '10']
<class 'int'>
[2020, 8, 10]
'''