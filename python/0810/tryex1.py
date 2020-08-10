'''
Created on 2020. 8. 10.
@author: GDJ24
tryex1.py : 예외 처리
'''
mystr = "파이썬 너무쥬아여. 맨날맨날 파이썬 했으면 좋겠당"
strpos = [] #파이썬 문자의 위치 정보 저장
index = 0
while True : #무한 loop
    #index = mystr.find("파이썬",index)
    #if index == -1 :
    #    break
    try :
        index = mystr.index("파이썬",index) #index(찾을내용, 몇 번째부터 찾을지)
        strpos.append(index) #strpos라는 list에 index가 0,16 이렇게 추가된다.
        index += 1
    except :
        break

print("파이썬 문자의 위치 :",strpos,",문자 개수 :",len(strpos))
