'''
Created on 2020. 8. 11.
@author: GDJ24
classex3.py : 상속, 오버라이딩
상속 할때는 파라미터 안에 클래스명을 쓰면 자동 상속된다.
다중상속도 가능하다.
'''

class Car :
    speed = 0
    room = 3
    door = 3
    def upSpeed(self,value):
        self.speed += value
        print("현재 속도(부모클래스): %d" % self.speed)
        
class Sedan(Car): # 상속표현
    pass # pass 추가 멤버변수가 없음을 의미 -> Car와 똑같다. 자바랑 같이 생각하면 {} 처럼 빈내용 이라고 생각하면 된다.

class Truck(Car):
    def upSpeed(self, value):
        self.speed += value
        if self.speed > 150 :
            self.speed = 150
            print("현재속도(자손클래스): %d" % self.speed)
            
class Container :
    room = 1
class MovingCar(Container, Car): #다중 상속
    pass

sedan1 = Sedan()
truck1 = Truck()
print("트럭:",end="")
truck1.upSpeed(200)
print("승용차:",end="")
sedan1.upSpeed(200)

mcar = MovingCar() #Container랑 Car를 다중상속한 클래스이다.
mcar.upSpeed(60)
print("이동차량의 방개수: ",mcar.room,", 문의 개수:",mcar.door)


