'''
Created on 2020. 8. 5.
@author: GDJ24
exam3.py : 숫자를 입력받아 입력된 값까지의 합, 짝수 합, 홀수합 구하기
'''


scan = int(input("숫자 입력:"))

sum = 0
for i in range(1,scan+1) :
    sum += i
print(sum)

even = 0
for i in range(0,scan+1,2):
    even +=i
print(even)

odd = 0
for i in range(1,scan+1,2):
    odd +=i
print(odd)