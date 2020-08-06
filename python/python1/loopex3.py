'''
Created on 2020. 8. 6.
@author: GDJ24
loopex3.py : 랜덤 함수를 사용하여 숫자 맞추기
1. 1부터 99까지의 임의의 수를 저장
2. 화면에 숫자 입력
3. 입력된 수가 저장된 수보다 크면 작은 수를 입력하세요 메시지를 출력
입력된 수가 저장된 수보다 작으면 더 큰 수를 입력하세요 메시지를 출력
4. 저장된 수와 입력된 수가 같은 경우, 입력 건수를 화면에 출력하고 프로그램 종료
'''

import random #모듈 로드, 모듈의 멤버를 이용함
rnum = random.randrange(1,100)
i = 1
# True : 예약어, while 구문이 무한 반복된다.
while True :
    a = int(input("숫자를 입력하세요: "))
    if a > rnum :
        print("더 작은 수입니다.")
    elif a <rnum :
        print("더 큰 수 입니다.")
    else :
        print("정답입니다.")
        break #반복문을 벗어난다.
    i += 1
print("%d번 만에 맞췄습니다." % i) #마지막 else에 걸리는경우에만 break해서 역로 올 수 있다.(정답인 경우)
