'''
Created on 2020. 8. 5.
@author: GDJ24
exam2.py : 초를 입력받아 몇 시간 몇분 몇 초인지 코딩하기
'''

a=int(input("시간초 입력:"))
print(a//(60*60),"시간")
print((a%(60*60)//60),"분")
print(((a%(60*60)%60)),"초")


second = int(input("초입력:"))
print(second//3600,"시간",end="")
second %= 3600;
print(second//60, "분",second%60,"초")

# %=를 하는 순간 변수의 값이 변경되는구나
