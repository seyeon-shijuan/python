'''
Created on 2020. 8. 11.
@author: GDJ24
classex1.py : 클래스
기본 생성자 : 생성자를 구현하지 않으면 시스템에서 제공하는 생성자
def __init__(self) -> 기본 생성자 형태
self 는 자바의 this이다.
'''

class Car : 
    color = ""
    speed = 0
    
    #생성자
    #The sole purpose of __init__ is to initialize the values of instance members for the new object.
    def __init__(self,v1="",v2=0): # 기본 생성자 : __init__
        self.color = v1
        self.speed = v2
    
    def upSpeed(self,value):
        self.speed += value
    
    def downSpeed(self,value):
        self.speed -= value

myCar1 = Car() # def __init__(self,v1="",v2=0), 객체화
myCar1.color = "빨강"
myCar1.speed = 0
myCar1.upSpeed(30)
myCar1.upSpeed(40)
myCar1.downSpeed(10)
print("자동차1 색상: %s, 속도: %dkm" % (myCar1.color,myCar1.speed)) # 자동차1 색상: 빨강, 속도: 60km

myCar2 = Car("파랑",50)
myCar2.downSpeed(10)
print("자동차2 색상: %s, 속도: %dkm" % (myCar2.color,myCar2.speed)) # 자동차2 색상: 파랑, 속도: 40km

myCar3 = Car("노랑") # 값을 안 넣으면 v2 의 기본값인 0으로 설정된다
myCar3.upSpeed(20)
print("자동차3 색상: %s, 속도: %dkm" % (myCar3.color,myCar3.speed)) # 자동차3 색상: 노랑, 속도: 20km


