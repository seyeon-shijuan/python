'''
Created on 2020. 8. 7.
@author: GDJ24
setex1.py : set(집합 클래스) 예제 -> {}
'''

set1 = {1,2,3,4,5} #{1, 2, 3, 4, 5}
print(set1)
set2 = {1,2,3,4,5,1,2,3,4,5} #{1, 2, 3, 4, 5} 중복해서 넣으면 덮어쓰이기만 한다. 밴다이어그램의 집합에 2개의 identical한 값이 들어올 수 없다.
print(set2)
set3 = {5,6,7,8}
print(set3) #{8, 5, 6, 7} 순서가 정해지지 않고 밴다이어그램의 집합처럼 놓여있다.


#교집합
print('set1과 set3의 교집합',set1 & set3) #set1과 set3의 교집합 {5}
print('set1과 set3의 교집합',set1.intersection(set3)) #set1과 set3의 교집합 {5}

#합집합
print("set1과 set3의 합집합",set1 | set3) #set1과 set3의 합집합 {1, 2, 3, 4, 5, 6, 7, 8}
print("set1과 set3의 합집합",set1.union(set3)) #set1과 set3의 합집합 {1, 2, 3, 4, 5, 6, 7, 8}




