'''
Created on 2020. 8. 7.
@author: GDJ24
dictionaryex2.py : 
'''
foods = {"떡볶이":"오뎅","짜장면":"단무지","라면":"김치","맥주":"치킨"}
for i in foods.keys() : #map.keySet()
    print("%s=>%s" % (i,foods[i]))

#화면에서 음식을 입력받아 궁합음식 출력하기
while True :
    myfood = input(str(list(foods.keys()))+"중 음식이름을 입력하세요: ") #문자열형태로 바꿔서 "중 음식이름을 입력하세요랑합치려고 최외측에 str() 한다.
    if myfood == "종료" :
        print("등록된 음식 개수:"+str(len(foods)))
        print("좋아하는 음식:"+str(list(foods.keys())))
        print("궁합음식:"+str(list(foods.values())))
        print(list(foods.items())) #map.entrySet() 
        #[('떡볶이', '오뎅'), ('짜장면', '단무지'), ('라면', '김치'), ('맥주', '치킨')] 튜플
        break
    if myfood in foods : #myfood 값이 foods의 key에 존재?
        print("<%s> 궁합음식은 <%s>입니다." % (myfood,foods[myfood]))
    else :
        print("존재하지 않는 음식입니다.")
        yn = input("그럼 등록하시겠어요? (Y)")
        if yn == "Y" or yn == "y" :
            f = input("궁합음식을 입력하세요")
            foods[myfood] = f 