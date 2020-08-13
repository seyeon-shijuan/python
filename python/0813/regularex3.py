'''
Created on 2020. 8. 13.
@author: GDJ24
regularex3.py : 정규식
'''


import re

str = "The quick brown fox jumps over the lazy dog. Te Thhe Thhe."
str_list = str.split()
pattern = re.compile("Th+e")
count = 0
for word in str_list :
    if pattern.search(word) : #pattern에 맞는 문자?
        count += 1
print("output 1 : {1:s}:{0:d} ".format(count, "개수")) #0번 패러미터가 두번째에 오고 1번 패러미터가 앞쪽으로 나오는 포맷이다.

#Te Thhe Thhe. 를 붙이면 output 1 : 개수:3  개수가 1에서 3으로 바뀐다.

#pattern = re.compile("Th/e")로 바꾸면 output 1 : 개수:2 가 된다.
#pattern = re.compile("Th*e")로 바꾸면 output 1 : 개수:4 가 된다.


#re.I : 대소문자 구분 없이.(Ignore case)
pattern = re.compile("Th*e",re.I)
count = 0
for word in str_list :
    if pattern.search(word) : #pattern에 맞는 문자?
        count +=1
print("output 2: {1:s}:{0:d} ".format(count, "개수")) #output 2: 개수:5 


pattern = re.compile("(?P<match_word>Th*e)",re.I) #여기에 re.I 이거 지우면 4개된다 소문자 포함이 안되어서
print("output 3 :", end="")
for word in str_list :
    if pattern.search(word) : #pattern에 맞는 문자?
        print("{0}".format(pattern.search(word).group("match_word")),end=",") #output 3 :The,the,Te,Thhe,Thhe,

print()
#pattern.sub : pattern이 맞는 문자열을 지정한 문자로 치환
str_find = "Th*e"
pattern = re.compile(str_find,re.I)
print("output 4 : {0}".format(pattern.sub("a",str))) #output 4 : a quick brown fox jumps over a lazy dog. Te Thhe Thhe.

