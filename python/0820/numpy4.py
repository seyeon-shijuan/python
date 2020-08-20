'''
Created on 2020. 8. 20.
@author: GDJ24
numpy4.py : 배열의 연결 및 분할
'''

import numpy as np
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[3,2,1],[6,5,4]])
print(x)
'''
[[1 2 3]
 [4 5 6]]
'''
print(y)
'''
[[3 2 1]
 [6 5 4]]
'''
#배열의 연결
print(np.concatenate([x,y],axis=0)) #행으로 연결 : 수직연결
'''
[[1 2 3]
 [4 5 6]
 [3 2 1]
 [6 5 4]]
'''
print(np.concatenate([x,y],axis=1)) #열로 연걸 : 수평 연결
'''
[[1 2 3 3 2 1]
 [4 5 6 6 5 4]]
'''

#형태가 다른 배열의 연결
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[1,2,3],[4,5,6],[3,2,1]])
z = np.array([[7],[10]])
print(np.vstack([x,y])) #vertical stack : column 길이가 같으면 된다.
'''
[[1 2 3]
 [4 5 6]
 [1 2 3]
 [4 5 6]
 [3 2 1]]
'''
print(np.hstack([x,z])) #horizontal stack : row 개수가 같으면 된다.
'''
[[ 1  2  3  7]
 [ 4  5  6 10]]
'''

print("★")
#배열의 분리
#0~15까지의 값을 4행4열 배열로 재배치하기
x = np.arange(16).reshape((4,4))
print(x)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
'''
upper,lower = np.vsplit(x,[2]) #2행을 기준으로 분리해서 upper과 lower로 옮긴다. 4행 4열짜리가 2x4, 2x4로 잘린다.
print(upper)
'''
[[0 1 2 3]
 [4 5 6 7]]
'''
print(lower)
'''
[[ 8  9 10 11]
 [12 13 14 15]]
'''
left,right = np.hsplit(x,[2]) # 2열(column)을 기준으로 분리해서 left와 right으로 옮긴다. 4행 4열짜리가 4x2, 4x2로 잘린다.
print(left)
'''
[[ 0  1]
 [ 4  5]
 [ 8  9]
 [12 13]]
'''
print(right)
'''
[[ 2  3]
 [ 6  7]
 [10 11]
 [14 15]]
'''