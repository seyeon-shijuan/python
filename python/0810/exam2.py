'''
Created on 2020. 8. 10.
@author: GDJ24
exam2.py : 문자열 문제
'''

#1번문제> 홍#길#동#으로 출력하기
ss = "이지은"
for i in range(len(ss)) :
    print(ss[i],end="#")
print() # 이#지#은#

#2번문제> 동길홍으로 출력하기
'''
for i in range(len(ss)-1,-1,-1) :
    print(ss[i],end="")
print()
'''
print(ss[::-1]) # 은지이


