'''
Created on 2020. 8. 5.
@author: GDJ24
loopex1.py : 반복문 연습
'''
from _ast import If
num = 0
while num < 5 :
    print(num,end=",") #0,1,2,3,4, 하고 num은 5가 되지만 출력은 안한다.
    num += 1
    
print("\nfor 구문") # 여기 n다음에 띄어쓰기하니까 진짜 띄어쓰기가 생김
for i in range(0,5) : # 벡터형 변수 0,1,2,3,4가 안에 들어감
    print(i,end=",") # range 범위 안에서 실행하고 바로 다음 값으로 넘어간다. for Each 처럼
    
print("\n")
#1부터 100까지의 합 구하기

sum = 0
for i in range(1,101) : #100을 range에 포함시켜야되서 101로 쓴다.
    sum += i
print("sigma 1-100 = ",sum) # 이 프린트는 for 구문 밖에 있다.

#1부터 100사이 짝수의 합을 구하기
even = 0
for i in range(1,101) :
    if(i%2==0) :
        even += i
print("sigma 1-100 with only even num = ",even)

even2 = 0
for i in range(0,101,2) : # 2간격으로
    even2 += i
print("sigma 1-100 with only even num = ",even2)
