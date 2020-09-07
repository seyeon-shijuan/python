'''
Created on 2020. 8. 25.
@author: GOODEE
0825/selenium3.py : 셀레니움을 이용하여 url 연결.
               url에서 제공되는 html 의 내용을 BeautifulSoup 모듈로 파싱
               pandas 모듈을 이용하여 csv 파일로 생성
'''
import time
import pandas as pd

from selenium import webdriver
from bs4 import BeautifulSoup 

driver = webdriver.Chrome("D:/20200224/setup/chromedriver")
driver.get('https://oscar.go.com/winners')

time.sleep(1)
# url이 전달하는 html 내용
html = driver.page_source
print(type(html))
soup = BeautifulSoup(html, 'html.parser')

category = soup.select \
('bls-winners-list > ul > li > div.winners-list__info > a')
movie = soup.select \
('bls-winners-list > ul > li > div.winners-list__info > h3 > a')
producer = soup.select \
('bls-winners-list > ul > li > div.winners-list__info > p')
print("category :",type(category))
print("movie :",type(movie))
print("producer :",type(producer))
oscars_2020 = []
# zip : 리스트 merge => 튜플
for item in zip(category, movie, producer):
    oscars_2020.append(
        #딕셔너리 객체로 생성
        {
              'category' : item[0].text,
              'movie'    : item[1].text,
              'producer' : item[2].text
        }
    )
data = pd.DataFrame(oscars_2020) #판다스 객체로 생성
print(data)
data.to_csv('oscars_win_2020.csv')
driver.quit()