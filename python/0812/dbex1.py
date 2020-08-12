'''
Created on 2020. 8. 12.
@author: GDJ24
dbex1.py : sqlite db 사용하기
'''

import sqlite3
dbpath ="test.sqlite"
conn = sqlite3.connect(dbpath) #test.sqlite라는 db에 연결한다. 없으면 만듦
cur = conn.cursor() #명령전달 객체
#여러 분장을 실행
cur.executescript(
    '''
    drop table if exists items;
    create table items (item_id integer primary key,
    name text unique,
    price integer);
    insert into items (name, price) values ('Apple',800);
    insert into items (name, price) values ('Orange',500);
    insert into items (name, price) values ('Banana',300);
    '''
    )
conn.commit() #transaction을 완료한다. 정상처리로. rollback 이라면 취소로 완료한다.
cur=conn.cursor()
cur.execute("select * from items")
item_list = cur.fetchall() #fetch 는 조회(select)의미
print(type(item_list))
for it in item_list :
    print(it)
    
    '''
(1, 'Apple', 800)
(2, 'Orange', 500)
(3, 'Banana', 300)
    '''
