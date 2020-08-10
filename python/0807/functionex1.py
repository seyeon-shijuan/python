'''
Created on 2020. 8. 7.
@author: GDJ24
functionex1.py : 자판기
'''

#함수선언
def coffee_machine(button):
    print()
    print("#1 물을 끓이고 있습니다.")
    print("#2 종이컵이 내려갑니다.")
    if button == 1 :
        print("#3 일반 커피를 내리고 있습니다.")
    elif button == 2 :
        print("#3 설탕 커피를 내리고 있습니다.")
    elif button == 3 :
        print("#3 블랙 커피를 내리고 있습니다.")
    else :
        print("#3 커피 종류를 선택하지 않았습니다. 기본 커피를 내립니다.")
    print("#4 물을 붓고 있습니다.")
    print("#5 완료되었습니다. 커피를 꺼내가세요.")
#함수의 끝
#main
coffee = int(input("커피를 선택하세요(1:보통,2:설탕,3:블랙)"))
coffee_machine(coffee)