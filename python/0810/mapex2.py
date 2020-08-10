'''
Created on 2020. 8. 10.
@author: GDJ24
mapex2 : 람다를 이용하여 map 처리하기
'''

mylist = [1,2,3,4,5]
#map을 이용하여 mylist 각각의 값에 10 더하기
add = lambda num:num+10
mylist = list(map(add,mylist))
print(mylist) #[11, 12, 13, 14, 15]
#for 구문 안쓰고 list() 안에 map(함수,적용할리스트명)으로 써서 바꿔도 된다.

'''
add = lambda num:num+10
for i in range(len(mylist)) :
    mylist[i] = (lambda num:num+10)(mylist[i])
print(mylist) #[21, 22, 23, 24, 25]
'''

mylist = list(map(lambda num:num-10,mylist))
mylist = list(map(lambda num:num*10,mylist))
print(mylist)

list1 = [1,2,3,4]
list2 = [10,20,30,40]
#hap = lambda n1,n2:n1+n2
#haplist = list(map(hap,list1,list2)) # list() 이거는 리스트를 만드는 함수고 안의 내용대로 리스트가 만들어진다.
#map()이거는 map(적용할 function-data type이 되도 된다, iterables 복제대상인 리스트를 넣으면 된다.)
#if former function requires more than 2 variables, you should put equally multiple lists with commas 
haplist = list(map(lambda n1,n2:n1+n2, list1,list2))
#이렇게 람다식을 바로 만들어서 좌변의 function 칸에 집어넣어도 된다. 그러면 한 줄 로 쓸 수 있음.
print(haplist) #[11, 22, 33, 44]

haplist = list(map(lambda n1,n2,n3:n1+n2+n3,mylist,list1,list2))
print(haplist) #[21, 42, 63, 84]
print(mylist) #[10, 20, 30, 40, 50] 가장 작은 값으로 출력된다.


