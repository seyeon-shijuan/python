'''
Created on 2020. 8. 11.
@author: GDJ24
strex3.py : 문자열 연습
'''
instr = input("문자를 입력하세요")
if instr.isdigit() :
    print("숫자입니다.")
elif instr.isalpha() :
    print("문자입니다.")
elif instr.isalnum() :
    print("문자+숫자입니다.")
else :
    print("그외 문자입니다.")
    
if instr.islower() :
    print("소문자입니다.")
elif instr.isupper() :
    print("대문자입니다.")
elif instr.isspace() :
    print("공백입니다.")
else :
    print("모릌ㅋㅋ겠습니다.ㅋㅋㅋ")
