'''
Created on 2020. 8. 12.
@author: GDJ24
regularex2.py : 정규식 사용하기
()그룹화 설정
{} 개수
\d : 숫자
(\d{6,7}[-]\d{7} :
    첫번째 그룹 : 숫자 6 혹은 7자리
    문자 -
    7자리 숫자
\g<1> : 첫 번째 그룹

?: 0 또는 1개
ca?t : a 문자가 없거나 1개이 경우
"ct": true
"cat" : true
"caaaat": true

* : 0개 이상
ca*t : a 문자가 0개 이상
"ct" : true
"cat": true
"caaat" : true

+ : 1개이상
ca+t : a 문자가 1개 이상
"ct" : false
"cat" : true
"caaaat" : true

{n} : n개 반복
ca{2}t : a 문자가 2개
"ct" : false
"cat": false
"caat": true
"caaaat": false

{n,m} : n개이상 m개 이하
ca{2,5}t : a 문자가 2개 이상 5개 이하
"ct" : false
"cat" : false
"caat": true
"caaat": true
"caaaaat" : true
"caaaaaaaaaaat": false

'''

import re #정규식 사용을 위한 모듈을 불러온다.

data = '''
    park 800805-1234567
    kim 700905-2345678
    choi 750905-a123456
'''
#re.compile(pattern) : 패턴에 맞는 문자열만 정규식의 대상이 된다.
pat = re.compile("(\d{6,7})[-]\d{7}") #[]는 optional이다. 있어도 되고 없어도 된다.
print(pat.sub("\g<1>-*******",data)) #\g는 그룹을 의미한다. 1번째 그룹은 놔두고 나머지는 -*******로 바꾸는 것으로 설정한다.

'''

    park 800805-*******
    kim 700905-*******
    choi 750905-a123456
'''


