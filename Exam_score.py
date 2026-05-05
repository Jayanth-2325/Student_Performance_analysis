import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Student_Performance.csv")
df["Study_level"]=pd.cut(df['Hours_Studied'],bins=[0,5,10,15,20], labels=['Low','Medium','High','Very High'])
df.groupby('Study_level')['Exam_Score'].mean().plot(kind='bar')
plt.title('Exam score based on study hours')
plt.xticks(rotation=0)
plt.xlabel("Study level")
plt.ylabel("Average exam score")
plt.savefig('Examstudylevel.png')
plt.show()