'''
Created on 2020. 8. 10.
@author: GDJ24
functionex3.py : 1. 리턴값을 두 개 이상 반화 -> 리스트로 반환 2. 가변매개변수 함수 
'''

def multi(v1,v2) :
#    list = []
    res1 = v1+v2
    res2 = v1-v2
    list.append(res1)
    list.append(res2)
    return list

def multiParam(* p): #  * 별을 그리면 안에 변수는 0개일 수도 , 여러 개일 수도 있다. whatever p(variable)이다.
    result = 0
    for i in p :
        result += i
    return result

list = []
hap,sub = 0,0
#list = multi(100,200)
multi(100,200)
hap = list[0]
sub = list[1]
print("multi 함수의 리턴 : %d, %d " % (hap, sub)) #multi 함수의 리턴 : 300, -100 

print("multiParam()=",multiParam()) #multiParam()= 0 parameter가 안들어갔을 때 return 될 값인 result를 지역변수로 0이라고 설정해 놓았기 때문에 0이 return 된다.
print("multiParam(10)=",multiParam(10)) #multiParam(10)= 10
print("multiParam(10,20)=",multiParam(10,20)) #multiParam(10,20)= 30
print("multiParam(10,20,30)=",multiParam(10,20,30)) #multiParam(10,20,30)= 60
