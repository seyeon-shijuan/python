'''
Created on 2020. 8. 24.
@author: GOODEE
0824/soupex3.py : 내가 만든 html 파일  분석하기
'''
from bs4 import BeautifulSoup

fp = open("books.html",encoding="utf-8")
soup = BeautifulSoup(fp,"html.parser")
print(soup.select("li")[3].string)
print(soup.find_all("li")[3].string)

#람다식을 이용하여 출력하기
sel = lambda q : print(soup.select_one(q).string)
# id="nu"인 태그의 값을 출력
sel("#nu")
# id="nu"인 li 태그의 값을 출력
sel("li#nu")
# ul 태그의 하위태그인 id="nu"인 li 태그의 값을 출력
sel("ul > li#nu")
sel("ul  li#nu")
# id="bible" 인 태그의  하위태그 중 id="nu"인  태그의 값을 출력
sel("#bible > #nu")
sel("#bible  #nu")

#li 태그 중 id="nu"인 태그의 값 출력
sel("li[id='nu']")
#li 태그 중 4번째 태그의 값 출력
sel("li:nth-of-type(4)")


