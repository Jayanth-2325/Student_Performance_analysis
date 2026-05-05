import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Student_Performance.csv")
df['After_pass']=df['Exam_Score']>70
result=df.groupby('Teacher_Quality')['After_pass'].mean()*100
result.plot(kind='bar')
plt.title('Percentage of student passed by Teacher quality')
plt.xlabel('Teacher Quality')
plt.xticks(rotation=0)
plt.ylabel('Percent of students')
plt.savefig('TeacherQuality.png')
plt.show()