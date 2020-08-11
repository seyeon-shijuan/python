'''
Created on 2020. 8. 11.
@author: GDJ24
classex2.py : 클래스 변수 사용하기
'''


class Car :
    color = ""
    speed = 0
    num = 0
    count = 0
    def __init__(self): #기본생성자
        self.speed = 0 #인스턴스 변수
        Car.count += 1 #클래스 변수
        self.num = Car.count
        
    def printMessage(self):
        print("색상:%s, 속도:%dkm, 번호:%d, 생산번호:%d" % (self.color,self.speed,self.num,Car.count))
        

mycar1,mycar2 = None, None #null, 참조 객체가 없음
mycar1 = Car() #객체화
mycar1.color = '애쉬그레이'
mycar1.speed = 30
mycar1.printMessage() #색상:애쉬그레이, 속도:30km, 번호:1, 생산번호:1


mycar2 = Car() #객체화
mycar2.color = '골드핑크'
mycar2.speed = 50
mycar2.printMessage() #색상:골드핑크, 속도:50km, 번호:2, 생산번호:2

#mycar3 = Car("빨강") #객체화. 오류 발생. 생성자 없음.
