'''
Created on 2020. 8. 13.
@author: GDJ24
csvex1.py : csv 파일 읽기
command 라인에서 입력 파일을 입력받기
'''

import sys
print(sys.argv[0])
infile = sys.argv[1] #cctv3.csv
outfile = sys.argv[2] #cctv2.csv
with open(infile,"r",newline="") as filereader : #뒤집어 표현
    with open(outfile,"w",newline="") as filewriter :
        header = filereader.readline()
        print(type(header))
        #headlist : list 형
        headlist = header.split(",")
        filewriter.write(",".join(map(str,headlist))+"\r\n") # cctv2.csv에  comma(,)로 연결하여 write한다.
         #list로 만들고 ,로 나눠서 만든다.
        for rowlist in filereader :
            filewriter.write(rowlist)
            
#D:\Python\python\0813\csvex1.py
#<class 'str'>

