'''
Created on 2020. 8. 12.
@author: GDJ24
dbex2.py : 화면에ㅓ 내용을 입력받아 sqlite db에 내용 저장하기
'''

import sqlite3

dbpath = "test.sqlite"
con = sqlite3.connect(dbpath)
cur = con.cursor()
cur.executescript(
    '''
    drop table if exists usertable;
    create table usertable (userid varchar(15) primary key,
    username varchar(20), email varchar(30), year integer);
    '''
    )


