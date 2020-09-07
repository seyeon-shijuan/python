'''
Created on 2020. 8. 24.
@author: GOODEE
0824/graph2.py : 그래프 여러개 작성하기
'''
import numpy as np
import matplotlib.pyplot as plt
# fig : 도화지. 2행2열로 분리 
# ax_lst : 각각의 이미지의 리스트
# figsize=(8,5) : 그래프 크기 지정
fig, ax_lst = plt.subplots(2,2,figsize=(8,5))
fig.suptitle("figure sample plots")
ax_lst[0][0].plot([1,2,3,4])
# np.random.randn : 가우시안 표준 정규 분포에서 난수 matrix array로 리턴
ax_lst[0][1].plot(np.random.randn(4,10),
                  np.random.randn(4,10))
#linspace : 등차 수열
# np.pi : 원주율
ax_lst[1][0].plot(np.linspace(0.0,5.0),
                  np.cos(2*np.pi * np.linspace(0.0,5.0)))
ax_lst[1][1].plot([3,7],[5,4])
plt.show()


