'''
Created on 2020. 8. 20.
@author: GDJ24
graph1.py : 그래프 그리기
'''
import matplotlib.pyplot as plt

plt.style.use("ggplot")
subjects = ["java","JSP","SPRING","HADOOP","PYTHON"]
print(range(len(subjects)))
subjects_index = range(len(subjects))
print(type(subjects))
scores = [65,90,85,60,95]

#그래프 설정
fig = plt.figure() #도화지
ax1 = fig.add_subplot(1,1,1) #도화지 분할: 1개의 도화지에 1행 1열 ->1개만
#bar = 바그래프
ax1.bar(subjects_index,scores,align="center", color="darkblue") #align이 center면 히스토그램처럼 붙지 않고 가운데 정렬됨
ax1.xaxis.set_ticks_position("bottom") #x축은 바닥에
ax1.yaxis.set_ticks_position("left") #y축은 왼쪽에

plt.xticks(subjects_index,subjects,rotation=0,fontsize="small") #x축 설정(range(0,5), ["java","JSP",...], rotation=0, fontsize="small"
plt.xlabel("Subject")
plt.ylabel("Score")
plt.title("Class Score")
plt.savefig("bar_plot.png", dpi=400, bbox_inches="tight")
plt.show() #화면에 ggplot이 나오게된다.
