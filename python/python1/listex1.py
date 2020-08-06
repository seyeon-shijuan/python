'''
Created on 2020. 8. 6.
@author: GDJ24
listex1.py : 리스트 예제(배열)
파이썬 리스트(list) => []
자료구조 dictionary(Map) => {key, value}
set(집합) => {value}
튜플(상수인 리스트) => ()
'''
a = [0,0,0,0]
b = []
print(b,len(b)) #[] 0
print(a,len(a)) #[0, 0, 0, 0] 4

suma,sumb=0,0
for i in range(0,len(a)) :
    a[i] = int(input(str(i+1)+"번째값:")) #str()문자열로 변경
    suma += a[i]
    b.append(a[i]) # b 리스트에 값을 추가, 자바함수 : add 함수
    sumb += b[i]
print(a,len(a))
print(b,len(b))
print("a 리스트의 합계:",suma)
print("b 리스트의 합계:",sumb)

'''
1번째값:10
2번째값:20
3번째값:30
4번째값:40
[10, 20, 30, 40] 4
[10, 20, 30, 40] 4
a 리스트의 합계: 100
b 리스트의 합계: 100
'''

print(a[::-1]) # 역순으으로 출력하기 [40, 30, 20, 10]