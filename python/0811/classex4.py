'''
Created on 2020. 8. 11.
@author: GDJ24
classex4.py : 클래스에서 사용되는 메서드
'''

class Line :
    length =0
    def __init__(self,length):
        self.length = length
    # 자바의 toString와 같은 메서드 기능
    def __repr__(self):
        return "선의 길이:" +str(self.length)
    def __add__(self,other): #객체간 + 연산자를 사용하면 호출되는 메서드 -> 연산자 오버로딩
        print("더하기 연산이 수행됩니다.")
        return self.length + other.length
    def __lt__(self,other):
        print("< 연산자가 호출됩니다.")
        return self.length < other.length
    def __gt__(self,other):
        print("> 연산자가 호출됩니다.")
        return self.length > other.length
    def __eq__(self,other):
        print("= 연산자가 호출됩니다.")
        return self.length == other.length
    def __del__(self): #소멸자 : 이 안의 self는 객체 자신을 의미한다.
        print(self.length,"길이의 선이 제거 되었습니다.")

myline1 = Line(200) #__init__ call (는 생성자) -> 객체를 생성하면 call되는 메서드
myline2 = Line(100)
print(myline1) #<__main__.Line object at 0x0382E6A0> 에서 __repr__만들면 선의 길이:200으로 바뀜 (ToString 표현 메서드 : 객체를 문자열 화 하는 것)
print(myline2) #<__main__.Line object at 0x03941DC0> 에서 __repr__만들면 선의 길이:100으로 바뀜 (ToString 표현 메서드 : 객체를 문자열 화 하는 것)

print("두선의 길이의 합:",myline1+myline2) #더하기 연산이 수행됩니다.두선의 길이의 합: 300
#TypeError: unsupported operand type(s) for +: 'Line' and 'Line' 기본적으로 클래스끼리 더할 수 가 없지
#그럴때  객체끼리 더했을 경우에 수행할 코드를 써넣은 __add__를 만들면 된다.

#두 선의 길이 비교하기
if myline1.length < myline2.length :
    print("myline2 선이 더 길어요")
elif myline1.length == myline2.length:
    print("두 선의 길이가 똑같아요.")
else :
    print("myline1 선이 더 길어요")
#실행결과 : myline1 선이 더 길어요

#두 선의 길이 비교하기 without myline1.length
if myline1 < myline2 : # __lt__  메서드가 call된다.
    print("myline2 선이 더 길어요!")
elif myline1 == myline2: #__eq__ 메서드가 call된다. False
    print("두 선의 길이가 똑같아요.")
elif myline1 > myline2 : #__gt__ 메서드 call된다. True
    print("myline1 선이 더 길어요")
#실행결과 : 비교 연산자가 호출됩니다.myline1 선이 더 길어요

#더이상 코드가 없으면 프로그램이 종료되고 Resource가 OS로 반납된다. 그래서 객체가 전부 소멸된다.
#200 길이의 선이 제거 되었습니다. > __del__ 은 객체가 소멸될때 수행하는 method이다. 내용이 다 끝나면 객체는 소멸하게 되는데 그때 수행할 코드가 있으면 이 __del__를 만들면 된다.
#100 길이의 선이 제거 되었습니다.

#소멸자는 overloading 할 수 없다.
