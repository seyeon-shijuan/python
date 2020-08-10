'''
Created on 2020. 8. 7.
@author: GDJ24
tupleex1.py : 튜플-변경할 수 없는 리스트
'''

tp1 = (10,20,30) #(10, 20, 30)
print(tp1)
print(tp1[0],tp1[1],tp1[2]) #10 20 30
#tp1.append(100)
#print(tp1)
'''
    tp1.append(100)
AttributeError: 'tuple' object has no attribute 'append' <-
'''
#tp1[0] = 100
#print(tp1)
'''
Traceback (most recent call last):
  File "D:\Python\python\0807\tupleex1.py", line 16, in <module>
    tp1[0] = 100
TypeError: 'tuple' object does not support item assignment
'''

list = list(tp1)
list.append(100) #[10, 20, 30, 100]
list[0] = 100
print(list,'★')
#list로 변경해서 append 하면 된다.

print(list)
tp1 = tuple(list) #튜플 <- 리스트
print(tp1)

print("tp1의 크기:",len(tp1),", list의 크기",len(list)) #tp1의 크기: 4 , list의 크기 4
print("tp1[1:3]:",tp1[1:3],",list[1:3]:",list[1:3]) #tp1[1:3]: (20, 30) ,list[1:3]: [20, 30]
print("tp1[1:3]:",tp1[:3],",list[1:3]:",list[:3]) #tp1[1:3]: (100, 20, 30) ,list[1:3]: [100, 20, 30]
print("tp1[2:]:",tp1[2:],", list[2:]:",list[2:]) #tp1[2:]: (30, 100) , list[2:]: [30, 100]
print("tp1[::2]:",tp1[::2],", list[::2]:",list[::2]) #tp1[::2]: (100, 30) , list[::2]: [100, 30]




