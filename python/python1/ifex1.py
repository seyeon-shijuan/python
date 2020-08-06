'''
Created on 2020. 8. 5.
@author: GDJ24
ifex1.py : if 조건문 예제
'''

score = 80
if score >= 90 :
    print("A학점")
else :
    if score >= 80 :
        print("B학점")
    else :
        if score >= 70 :
            print("C학점")
        else:
             if score >= 60 :
                 print("D학점")
             else:                                        
                print("F학점")
                # else : if면 한칸씩 들여쓴다.

print("if elif 구문으로 변경하기")
if score >= 90 :
    print("A학점")
elif score >=80 :
    print("B학점")
elif score >=70 :
    print("C학점")
elif score >=60 :
    print("D학점")
else :
    print("F학점")
    
    # elif 면 들여쓰기 없음 else까지도 없음
    