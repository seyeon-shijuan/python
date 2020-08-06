'''
Created on 2020. 8. 6.
@author: GDJ24
strex1.py : 문자열 처리, 문자열을 배열로 처리 가능함
'''
#문자의 리스트임, python에는 배열이 없다.
print("annyeonghaseyo")
print("annyeonghaseyo"[0]) #a
print("annyeonghaseyo"[4]) #e
print("annyeonghaseyo"[-1]) #o 1번문자열에서 뒤로 1칸간다.->제일 마지막글자로 돌아감
print("annyeonghaseyo"[-2]) #y

#부분 문자열
print("annyeonghaseyo"[1:3]) #1번인덱스부터 3번인덱스 사이까지 나온다. 1,2만 나옴 (맨뒤는 포함x) nn
print("annyeonghaseyo"[:3])#처음부터 3번인덱스사이까지 나온다 ann
print("annyeonghaseyo"[3:])#3번인덱스부터 끝까지 나온다 yeonghaseyo
print("이지금짱짱걸"[::2])#2칸씩 부분문자열 anenhsy '이' 지 '금' 짱 '짱' 걸
print("이지금짱짱걸"[::-1])#역순으로 출력 걸짱짱금지이
print("이지금짱짱걸"[::-2])#역순 2칸 간격으로 출력 걸짱지

#함수
print(type("이지금짱짱걸")) #자료형 확인 <class 'str'>
print(len("이지금짱짱걸")) #문자열의 글자길이 확인 6

a="hello"
cnt = 0;
# l 문자의 개수를 출력하기
for i in range(0,len(a)) :
    if(a[i] == 'l') :
        cnt += 1
print("L이",cnt,"개") #l이 2 개

print("L이",a.count('l'),"개") #L이 2 개
print("a위치=",a.find('a')) #a위치= -1
print("l위치=",a.index('l')) #l위치= 2


