'''
Created on 2020. 8. 11.
@author: GDJ24
comprehensionex1.py : 컴프리헨션 예제
패턴이 있는 list, dictionary, set을 간편하게 작성할 수 있는 기능
'''

numbers = []
for n in range(1,11) :
    numbers.append(n)
print(numbers)

#컴프리헨션 표현
print([x for x in range(1,11)])
clist = [x for x in range(1,11)]
#[] 이 표시가 list이다.
print(clist)

# 1~10 까지 짝수 리스트 생성
evenlist = []
for n in range(1,11) :
    if n% 2 ==0 :
        evenlist.append(n)
print(evenlist)
#컴프리헨션 표현
evenlist = [ x for x in range(1,11) if x%2 == 0]
print(evenlist)

#2의 배수이고, 3의 배수인 값만 리스트에 추가하기
evenlist = [x for x in range(1,11) if x%2 == 0 if x%3 == 0]
#그냥 바로 띄어쓰기 하고 if문 또 쓰면 된다. && 할 필요 없음.
print(evenlist)

#컴프리헨션 중첩하기
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
list1 = []
list1 = [x for row in matrix for x in row]
print(list1)
#이거 이해 잘 안가는데???



