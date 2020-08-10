'''
Created on 2020. 8. 10.
@author: GDJ24
exam1.py : 피보나치 수열 출력하기
피보나치 수열의 요소 개수를 입력하세요(3이상의 값) : 5
[0,1,1,2,3,5,8,13,21,34]
'''
def fibo(n) :
    f=1
    list= [0]
    for i in range(1,n) :
        list.append(list[i-1]+f)
        f=list[i-1]
    return list
num =  int(input("피보나치 수열의 요소 개수를 입력하세요 (3이상의 값): "))
print("f(",num,")=",end="")
print(fibo(num))

'''
피보나치 수열의 요소 개수를 입력하세요 (3이상의 값): 10
f( 10 )=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
꺙 너무 재밌어 ><
'''