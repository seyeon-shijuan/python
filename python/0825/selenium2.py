'''
Created on 2020. 8. 25.
@author: GOODEE
0825/selenium2.py : 네이버 로그인하기
'''
import time
from selenium import webdriver

#크롬 브라우저 로드
driver = webdriver.Chrome("D:/20200224/setup/chromedriver")
time.sleep(1)
# url 설정 
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
id = input("네이버 아이디를 입력하세요:")
# javascript 실행.
driver.execute_script
("document.getElementsByName('id')[0].value='"+id+"'")
pw = input("네이버 비밀번호를 입력하세요:")
driver.execute_script
("document.getElementsByName('pw')[0].value='"+pw+"'")
# find_element_by_xpath : xpath이용하여 지정한 태그객체 한개에 접근.
# click() : 클릭이벤트 발생.=> 버튼 클릭효과
driver.find_element_by_xpath('//*[@id="log.login"]').click()