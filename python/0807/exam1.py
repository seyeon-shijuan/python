'''
Created on 2020. 8. 7.
@author: GDJ24
exam1.py : 나라와 수도를 입력하고 화면에 나라이름을 입력받아 해당 나라의 수도를 출력하기
등록된 나라가 아닌 경우 수도를 입력받아 등록하기
나라 입력시 "종료" 입력하면 프로그램 종료
종료후 등록된 모든 나라와 수도 정보가 화면에 표기
'''
country = {'대한민국':'서울','영국':'런던','중국':'베이징','미국':'워싱턴DC','대만':'타이베이','일본':'도쿄'}

while True:
    city = input(str(list(country.keys()))+"중 입력:")
    if city == "종료":
        print("등록된 국가:" +str(len(country)))
        print("국가:"+str(list(country.keys())))
        print("수도:"+str(list(country.values())))
        break
    if city in country :
        print("<%s>의 수도는 <%s>입니다." %(city,country[city]))
    else :
        print("등록되지 않은 국가입니다.")
        yn = input("그럼 등록하시겠어요? (y or no)")
        if yn == "Y" or yn == "y" :
            f= input("수도 입력:")
            country[city] = f