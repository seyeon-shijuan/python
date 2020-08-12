'''
Created on 2020. 8. 12.
@author: GDJ24
classex5.py : 추상 메서드 예제 -> 자손 클래스에서 반드시 오버라이딩 필요
'''

class SuperClass :
    def method(self): #추상메서드
        raise NotImplementedError #자손 클래스에서 오버라이딩 해야 함
    # method를 define하고나서 아무것도 안쓰고 raise NotImplementedError 쓰면 추상메서드가 된다.
    
class SubClass1(SuperClass):
    def method(self):
        print("SubClass1 에서 method()를 오버라이딩 함")

class SubClass2(SuperClass):
    def method(self):
        print("SubClass2 에서 method()를 오버라이딩 함")
        
su = SuperClass()
print(su) #<__main__.SuperClass object at 0x0090E6A0> 객체화는 되었다.
#su.method() #raise NotImplementedError #자손 클래스에서 오버라이딩 해야 함 NotImplementedError

sub1 = SubClass1()
sub2 = SubClass2()
sub1.method()
sub2.method()