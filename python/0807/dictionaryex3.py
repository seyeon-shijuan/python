'''
Created on 2020. 8. 7.
@author: GDJ24
dictionaryex3.py :
'''
import operator

dic,list = {},[]
dic = {'Thomas':'토마스','Edward':'에드워드','Henry':'헨리','Gothen':'고든','James':'제임스'}
#sorted : 정렬하기
#dic.items() : 내부의 튜플 객체
#operator.itemgetter(0) : 튜플 객체의 첫 번째 엘리먼트가 정렬의 기준이 된다. >Thomas, Edward..
#reverse=True : 내림차순으로 바꾼다. Thomas, James..
list = sorted(dic.items(), key=operator.itemgetter(0),reverse=True) #[('Thomas', '토마스'), ('James', '제임스'), ('Henry', '헨리'), ('Gothen', '고든'), ('Edward', '에드워드')]
print(type(list)) #<class 'list'>
print(list)

#operator.itemgetter(1) : 튜플 객체의 두 번째 엘리먼트가 정렬의 기준이 된다. >고든, 에드워드 ..
list = sorted(dic.items(), key=operator.itemgetter(1), reverse=False) #[('Gothen', '고든'), ('Edward', '에드워드'), ('James', '제임스'), ('Thomas', '토마스'), ('Henry', '헨리')]
print(list)