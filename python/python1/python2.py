'''
Created on 2020. 8. 5.

@author: GDJ24
python2.py : input(), print() 함수
input("입력전출력문자열") : 입력받은 값은 문자열 형태로 입력받는다.
print(출력값1,출력값2, ...) : 여러개 출력시 ,로 연결할 수 있다.
'''
a = int(input("값1 입력: "))
b = int(input("값2 입력: "))
result = a + b;
print(a, "+", b, "=", result)

#print(a+"+"+b+"="+result) # 오류 발생
print("%d + %d = %d" % (a,b,result))
print("{0:d} + {1:d} = {2:d}".format(a,b,result))
print("안녕하세요", end="") #원래 모든 문장 끝에는 엔터키가 포함되어있는데 end를 쓰고 저렇게 하면 엔터안된다.
print("이지은 입니다.")

print("""Yellow CARD
이선 넘으면 침범이야 BEEP""")