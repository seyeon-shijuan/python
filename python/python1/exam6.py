'''
Created on 2020. 8. 6.
@author: GDJ24
exam6.py : 리스트 문제
aa,bb 배열을 생성하고 aa 배열은 0부터 짝수 20개를 저장한다.
bb 배열은 aa배열의 역순으로 값을 저장한다.
그리고 aa,bb 배열의 값을 출력하자
'''

aa=[]
bb=[]
value = 0

for i in range(0,20) :
    aa.append(value)
    value += 2
#for i in range(0,len(aa)) :
    #bb.append(aa[len(aa)-1-i])

for i in range(-1,-21, -1) :
    bb.append(aa[i])

print(aa)
print(bb)

#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
#[38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]