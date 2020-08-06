'''
Created on 2020. 8. 6.
@author: GDJ24
listex2.py : 리스트의 기본함수
'''

mylist= [30,10,20]
print("리스트: %s" % mylist)
mylist.append(40)
print("mylist.append(40) 후 리스트 : %s" % mylist) #mylist.append(40) 후 리스트 : [30, 10, 20, 40]

#pop() : stack은 last in first out이다. pop은 마지막 요소를 제거하고 제거한 값을 리턴한다.->40이 날라갔다고 보여준다.
print("pop() 메서드 결과: %s" % mylist.pop()) #pop() 메서드 결과: 40

print("mylist.pop() 후 리스트: %s" %mylist) #mylist.pop() 후 리스트: [30, 10, 20]
mylist.sort()
print("mylist.sort() 후 리스트: %s" % mylist) #mylist.sort() 후 리스트: [10, 20, 30]
mylist.reverse()
print("mylist.reverse() 후 리스트: %s" % mylist) #mylist.reverse() 후 리스트: [30, 20, 10]

print("20의 위치는? : %d" % mylist.index(20)) #20의 위치는? : 1
mylist.insert(2, 222) #2번째 인덱스(3rd)에 222를 끼워넣는다. ->4개됨
print("mylist.insert(2,222) 후 리스트 : %s" % mylist) #mylist.insert(2,222) 후 리스트 : [30, 20, 222, 10]
mylist.remove(222) #안에 parameter만 없앨 수 있다.
print("mylist.remove(222) 후 리스트 : %s" % mylist) #mylist.remove(222) 후 리스트 : [30, 20, 10]

mylist.extend([77,77,99]) # 뒤로 붙이기 / append는 요소 1개를 추가하기
print("mylist.extend([77,77,99]) 후 리스트 : %s" %mylist) #mylist.extend([77,77,99]) 후 리스트 : [30, 20, 10, 77, 77, 99]
print("77의 개수 : %d" % mylist.count(77)) #77의 개수 : 2

#리스트에서는 Find 사용 불가 > count만 쓰면 됨

