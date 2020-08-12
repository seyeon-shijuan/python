'''
Created on 2020. 8. 12.
@author: GDJ24
regularex2.py : 정규식 사용하기
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


