'''
Created on 2020. 8. 24.
@author: GOODEE
0824/soupex4.py : 네이버 페이지의 환율 정보 조회
'''
from bs4 import BeautifulSoup
import urllib.request as req
url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)
soup = BeautifulSoup (res, "html.parser", from_encoding="euc-kr")
# 클래스 속성이 head_info인 div
#hlist = soup.select("div.head_info") 
#htitle = soup.select("h3.h_lst")
# lambda 방식으로 변경하기
sel = lambda q : soup.select(q)
hlist = sel("div.head_info")
print(type(hlist))
htitle = sel("h3.h_lst")
a = [1,2,3,4,5]
b = ["a","b","c","d","e"]
for x in zip(a,b) : 
    print(x)
#zip : 두개의 리스트를 하나로 연결 함수
for tag, title in zip(hlist, htitle) :
    print(title.select_one("span.blind").string, end="\t")
    value = tag.select_one("span.value").string
    print(value, end=" ")
    change = tag.select_one("span.change").string
    print(change, end="\t")

    blinds = tag.select("span.blind")
    b = tag.select("span.blind")[-1].string
    print(b, end="*******\n")