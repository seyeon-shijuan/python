'''
Created on 2020. 8. 7.
@author: GDJ24
exam2.py : 배열의 값의 합과 평균을 구하는 함수 만들기
'''


def getSum(numlist):
    return sum(numlist)

def getMean(numlist):
    return sum(numlist)/len(numlist) if len(numlist) > 0 else 0

list = [2,3,3,4,4,5,5,6,6,8,8]
print("list 값의 합:",getSum(list)) #list 값의 합: 54
print("list 값의 평균:",getMean(list)) #list 값의 평균: 4.909090909090909

list2 = []
print("list 값의 합:",getSum(list2)) #list 값의 합: 0
print("list 값의 평균:",getMean(list2)) #list 값의 평균: 0
'''
Traceback (most recent call last):
  File "D:\Python\python\0807\exam2.py", line 20, in <module>
    print("list 값의 평균:",getMean(list2))
  File "D:\Python\python\0807\exam2.py", line 12, in getMean
    return sum(numlist)/len(numlist)
ZeroDivisionError: division by zero

> 뒤에  if len(numlist) > 0 else 0를 쓰면 해결된다
> 의미 : 영어 그대로 해석하면된다.
> if len(numlist) is greater than 0, return sum(numlist)/len(numlist) else(otherwise) return 0

> 아래줄을 위로 달라붙게하려면 \ 이거 쓰면 된다. (개행하고싶을 때 쓰면 된다.)
'''

tp = (2,3,3,4,4,5,5,6,6,8,8)
print("tp 값의 합:",getSum(tp)) #tp 값의 합: 54
print("tp 값의 평균:",getMean(tp)) #tp 값의 평균: 4.909090909090909



