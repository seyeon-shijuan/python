'''
Created on 2020. 8. 11.
@author: GDJ24
strex2.py : 문자열관련 함수
'''

ss = "(이지은"
#ss 문자열이 (로 시작하지 않으면 ( 추가
# )로 끝나지 않으면 ) 추가하여 (이지은)으로 출력하기

if ss.startswith("(") == False :
    print("(",end="")
print(ss,end="")
if ss.endswith(")") == False :
    print(")")

#문자열 분리하기
ss = "2020/08/11"
print(ss, "날짜의 10년 전을 출력하기")
list = ss.split("/")
print(int(list[0])-10,"년",list[1],"월",list[2],"일")
print(list)
