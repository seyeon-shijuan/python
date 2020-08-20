'''
Created on 2020. 8. 20.
@author: GDJ24
numpy3.py : numpy 예제 : 배열 사본 생성, 재구조화 예제
'''

import numpy as np
#0부터 9까지 임의의 난수 10개를 배열로 저장
x = np.random.randint(10, size =10) #[1 6 3 4 9 0 9 8 9 6]
x_sub = x[:2]
#In coding, knowing something or not knowing something is just a slight difference.
print(x) #[1 6 3 4 9 0 9 8 9 6]
print(x_sub) #[1 6]
x_sub[0] = 20 #사본(x_sub)의 0번째 요소를 20으로 바꾸면 원본(x)도 바뀜
print(x) #[20  6  3  4  9  0  9  8  9  6]
print(x_sub) #[20  6]

print('♥')

#배열 복사
x_cop = x.copy()
x_cop[0] = 100
print(x) #[20  0  0  6  7  9  6  0  8  7]
print(x_cop) #[100   0   0   6   7   9   6   0   8   7]

#배열의 재편성
x2  = x.reshape(5,2) # x : 1차원 배열 -: x2 : 5행2열의 2차원 배열로 재편성
print(x2)
'''
[[20  1]
 [ 8  2]
 [ 8  0]
 [ 3  8]
 [ 9  9]]
'''

# 0부터 9까지의 임의의 수를 9개 가지고 있는 배열 a를 3행 3열 짜리 배열로 재편성
x3 = np.random.randint(9, size=9)
x3 = x3.reshape(3,3)
print(x3,"★")
'''
[[4 7 6]
 [8 0 3]
 [6 8 3]] ★ 넘재미땅 ㅎㅎ
'''
