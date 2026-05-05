import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Student_Performance.csv")
total=df.groupby("Extracurricular_Activities")['Exam_Score'].mean()
total.plot(kind='bar')
plt.title("Extracurricular activites vs exam score")
plt.xlabel('Participation')
plt.xticks(rotation=0)
plt.ylim(50,80)
plt.ylabel('Average Score')
plt.savefig('ExtraActivitiesScore.png')
plt.show()