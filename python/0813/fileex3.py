'''
Created on 2020. 8. 13.
@author: GDJ24
fileex3 : 
'''
import os.path

file="fileex1.py"
file="../0813"
if os.path.isfile(file) :
    print(file,"은 파일입니다.")
elif os.path.isdir(file) :
    print(file,"은 폴더입니다.")

if os.path.exists(file) :
    print(file,"은 존재합니다.")
else :
    print(file, "이 존재하지 않습니다.")


'''
../0813 은 폴더입니다.
../0813 은 존재합니다.
'''

