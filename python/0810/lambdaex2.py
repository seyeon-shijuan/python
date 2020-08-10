'''
Created on 2020. 8. 10.
@author: GDJ24
lambdaex2.py : 람다식을 이용한 리스트 처리
'''
myList=[1,2,3,4,5]
def add10(num):
    return num+10

for i in range(len(myList)) :
    myList[i] = add10(myList[i])
print(myList) #[11, 12, 13, 14, 15]

#add = lambda num:num+10
for i in range(len(myList)) :
#    myList[i] = add(myList[i])
    myList[i] = (lambda num:num+10)(myList[i]) 
print(myList) #[21, 22, 23, 24, 25]


for i in range(len(myList)) :
    myList[i] = (lambda n:n*2)(myList[i])
print(myList) # [42, 44, 46, 48, 50]

this = lambda x,y:x*y
print(this(5,4)) #20

miList = [2,4,6]
for i in range(len(miList)) :
    miList[i] = (lambda n:n/2)(miList[i])
print(miList) #[1.0, 2.0, 3.0]