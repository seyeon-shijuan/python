'''
Created on 2020. 8. 12.
@author: GDJ24
dbex5.py : mariadb에 데이터 추가하기
'''

import pymysql
conn = pymysql.connect(host="localhost",port=3306,user="scott",passwd="1234",db="classdb",charset="utf8")
cur = conn.cursor() #명령을 전달해 주는 객체
data = [
    (12,"골드키위",3000,"골드키위도 별로 골드 컬러가 아니다."),
    (13,"아보카도",7000,"멕시코에서는 엄청 싼데 한국에서는 너무 비싼 것 같다."),
    (14,"용과",6000,"칼로 반을 잘라서 숫가락으로 떠먹으면 맛있다. 냉동은 별로.."),
    ] #tuple을 list로 만들었다.
for i in data :
    cur.execute(''' insert into item (id,name,price,description) values(%s, %s, %s, %s)''',i) #튜플은 알아서 1,2,3,4에 맞춰서 들어간다.
cur.execute("select * from item")
for row in cur.fetchall() :
    print(row)
conn.rollback()


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
(12, '골드키위', 3000, '골드키위도 별로 골드 컬러가 아니다.', None)
(13, '아보카도', 7000, '멕시코에서는 엄청 싼데 한국에서는 너무 비싼 것 같다.', None)
(14, '용과', 6000, '칼로 반을 잘라서 숫가락으로 떠먹으면 맛있다. 냉동은 별로..', None) 
'''