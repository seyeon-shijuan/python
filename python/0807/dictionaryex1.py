'''
Created on 2020. 8. 7.
@author: GDJ24
dictionaryex1.py : 딕셔너리 예제
'''

singer = {}
singer['이름']='트와이스' #map.put('이름','트와이스')
singer['구성원스']=9
singer['데뷔곡']='우아하게'
singer['소속사']='JYP' #map.put('소속사','JYP')
singer['소속사']='SM' #map.put('소속사','SM') 수정된다.
# singer.keys() : dictionary 의 key 값만 리턴
for i in singer.keys() :
    print("%s => %s" % (i,singer[i]))
    
print(singer) #{'이름': '트와이스', '구성원스': 9, '데뷔곡': '우아하게', '소속사': 'JYP'} Json 형태
print(type(singer)) #<class 'dict'>
print(type(singer.keys())) #<class 'dict_keys'>
print(str(list(singer.keys()))+"*****") #['이름', '구성원스', '데뷔곡', '소속사']*****
