'''
Created on 2020. 8. 6.
@author: GDJ24
loopex2.py : 중첩 반복문 예제. 구구단 출력
'''
i, j=0,0
for i in range(2,10) :
    print("%5d단" % i) #5칸 공백을 만들고 그 공백 안에 %다음에 들어오는내용을 우측정렬한다.
    for j in range(2,10) :
        print("%2d X %2d = %3d" % (i,j,(i*j)))
    print()
    
'''
       9단
 9 X  2 =  18
 9 X  3 =  27
 9 X  4 =  36
 9 X  5 =  45
 9 X  6 =  54
 9 X  7 =  63
 9 X  8 =  72
 9 X  9 =  81
 '''