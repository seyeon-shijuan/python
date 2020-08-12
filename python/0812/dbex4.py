'''
Created on 2020. 8. 12.
@author: GDJ24
dbex4.py : mariadb 연동하기
'''

import pymysql #pip install pymysql
conn = pymysql.connect(host="localhost",port=3306, user="scott",passwd="1234",db="classdb",charset="utf8")
try :
    cur = conn.cursor() #명령을 전달해 주는 객체
    cur.execute("select * from item")
    #for 구문을 이용한 컬럼 불러오기
#    for row in cur.fetchall() : #fetchall이 실행한다.
#        print(row[0],row[1],row[2])
    while True : #while 구문을 이용한 컬럼 불러오기
        row = cur.fetchone()
        if row == None : #조회된 레코드가 없으면
            break
        print(row)
finally :
    cur.close()
    conn.close()
    

'''
(1, '레몬', 50, '레몬에 포함된 구연산은 피로회복에 좋습니다.   비타민C 도 풍부합니다.', 'lemon.jpg')
(2, '오렌지', 100, '비타민C 가 풍부합니다. 맛도 좋습니다.', 'orange.jpg')
(3, '키위', 200, '비타민C 가 풍부합니다. 다이어트에 좋습니다.', 'kiui.jpg')
(4, '포도', 300, '폴리페놀을 다량 함유하고 있어 항산화 작용을 합니다.', 'podo.jpg')
(5, '딸기', 800, '비타민C를 다량 함유하고 있습니다.', 'ichigo.jpg')
(6, '귤', 1000, '시네피린을 다량 함유하고 있어 감기예방에 좋습니다.', 'mikan.jpg')
(8, '체리', 3000, '체리 3000원에 살 수 있으면 좋겠다...', 'cherry.JPG')
(9, '하미과', 1000, '하미과 멜론 1000원이면 좋겠다.★♥', 'hamigua.JPG')
(10, '체리톡톡', 1900, '버거킹 체리톡톡 씨그램+체리 JMT >D<', 'cherry.JPG')
(11, '유자', 2700, '유자인데 홍유자가 더 비싼데 맛있다...', 'yuzi.JPG')
'''