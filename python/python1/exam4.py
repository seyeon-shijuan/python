'''
Created on 2020. 8. 6.
@author: GDJ24
exam4.py : 삼각형 출력하기
삼각형의 높이를 입력받은 후 삼각형을 출력하는 프로그램을 작성하기
'''
a=int(input("삼각형의 높이를 입력하세요 :"))
for i in range(1, a+1) :
    print("*"*i)
'''
*
**
***
****
*****
'''
print("\n")

for i in range(1, a+1) :
    print("*"*(a+1-i))
'''
*****
****
***
**
*
'''
print("\n")


for i in range(a,0,-1) :
    print("*"*i)
'''
*****
****
***
**
*
'''    
print("\n")

for i in range(1, a+1) :
    print("  "*(a-i),"*"*(i))
'''
         *
       **
     ***
   ****
 *****
''' 
print("\n")

for i in range(1, a+1) :
    print("  "*(i-1),"*"*(a+1-i))
'''
 *****
   ****
     ***
       **
         *
''' 
print("\n")

for i in range(1, a+1) :
    print("  "*(a-i),"*"*(2*i-1))
'''
         *
       ***
     *****
   *******
 *********
''' 
print("\n")

for i in range(a, 0, -1) :
    print("  "*(a-i), "*"*(i*2-1))
'''
 *********
   *******
     *****
       ***
         *
''' 

