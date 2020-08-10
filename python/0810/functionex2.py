'''
Created on 2020. 8. 10.
@author: GDJ24
functionex2.py : 전역 변수 사용하기
'''

def func1() :
    global gval
    gval = 200
    a = 20 #지역변수
    b = 1000 #지역변수
    #지역변수는 자기 function 외부에서는 전혀 적용되지 않는다.
    print("func1() 함수가 호출되었습니다.",gval,a,b) 

def func2() :
    b = 2000
    print("func2() 함수 호출함",gval,a,b)
    func1()
    print("전역변수 gval 값=",gval,a,b) #100, 10

gval = 100 #전역변수 -> 모든 함수에서 사용이 가능한 변수
a =10
if __name__ == '__main__' : #프로그램의 시작
    func1() #func1() 함수가 호출되었습니다. 200 20 1000
    print("_main_ 함수가 호출되었습니다.",gval,a) #_main_ 함수가 호출되었습니다. 100 10
    #global gval 을 위에 선언하면 _main_ 함수가 호출되었습니다. 200 10
    #전역변수인 200을 사용한다.
    func2()  
    '''
    func2() 함수 호출함 200 10 2000 > gval, a, b가 call 된건데 전역, 전역, 지역이 호출됨
    func1() 함수가 호출되었습니다. 200 20 1000 > gval, a, b가 call 된건데 전역, 지역, 지역이 호출됨
    전역변수 gval 값= 200 10 2000 > 
    '''
    
    




