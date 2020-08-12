'''
Created on 2020. 8. 12.
@author: GDJ24
regularex1.py : 정규식 예제
'''

data = '''
    park 800805-1234567
    kim 700905-2345678
    choi 750905-a123456
'''
print(data.split("\n")) #['', '    park 800805-1234567', '    kim 700905-2345678', '    choi 750905-a123456', '']

result = []
for line in data.split("\n") :
    word_result = []
    for word in line.split(" ") :
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit() :
            word = word[:6]+"-"+"*********" #if 문에 걸리는경우에만 *처리되고 아닌 경우는 전부 바로 아래 커맨드가 실행된다.
        word_result.append(word) #if에 안걸리면 그냥 그대로 word_result에 추가된다.
    result.append("♥".join(word_result)) #word_result라는 list를 ♥로 구분하기
print("\n".join(result)) #result라는 list를 엔터로 구분하기

'''
♥♥♥♥park♥800805-*********
♥♥♥♥kim♥700905-*********
♥♥♥♥choi♥750905-a123456
'''