'''
Created on 2020. 8. 11.
@author: GDJ24
comprehensionex2.py : 컴프리헨션을 이용한 set
'''

set1 = {x**2 for x in [1,2,3]}
print(set1) #{1, 4, 9}

list1 = [x**2 for x in [1,1,2,2,3,3]]
print(list1) #[1, 1, 4, 4, 9, 9] 제곱되네

#1부터 10까지의 수 중에서 짝수의 제곱을 출력하기
print([x**2 for x in range(1,11) if x%2==0]) #[4, 16, 36, 64, 100]
#I am ingenious

set2 = {x**2 for x in range(1,11) if x%2==0}
print(set2)  #{64, 100, 4, 36, 16} 불규칙
print(sorted(set2, key=None, reverse=False)) #[4, 16, 36, 64, 100] 정렬하면 set에서 list로 바뀐다.


