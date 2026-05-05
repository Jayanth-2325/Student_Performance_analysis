import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Student_Performance.csv")
df['Top_exam']=df["Exam_Score"]>90
result=df.groupby('School_Type')['Top_exam'].mean()
result.plot(kind='pie',autopct="%1.1f%%")
plt.title("Above 90 marks score by school type")
plt.savefig('Schoolmarks.png')
plt.show()