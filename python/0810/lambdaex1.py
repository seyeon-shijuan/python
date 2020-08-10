'''
Created on 2020. 8. 10.
@author: GDJ24
lambdaex1.py : 람다식으로 함수 구현
'''

def hap(num1,num2):
    res = num1 + num2
    return res 

print(hap(10,20)) # 30
#람다 방식으로 구현
hap1 = lambda num1,num2:num1+num2 # in Java (num1,num2) ->(num1+num2)
print(hap1(10,20)) #30
#def 안써도 되고, 리턴을 위한 메모리 따로 할당 안해도 되고 필요한 변수를 놓고 바로 : 콜론 뒤에 계산식만 쓰면 된다.

#람다 방식으로 곱셈 결과 구현하기
mul1 = lambda n1,n2:n1*n2
print(mul1(10,20)) #200

#파라미터 초기화 하기
hap2 = lambda num1=0,num2=1:num1+num2
print(hap2()) #1 아무것도 안넣었을 때
print(hap2(100)) #101 첫 번째 거가 100으로 바뀌었을 때
print(hap2(100,200)) #300 첫 번째, 두 번째를 100,200으로 바뀌었을 때
