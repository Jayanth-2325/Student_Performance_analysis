import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('Student_Performance.csv')
df.groupby('Attendance')['Exam_Score'].mean().sort_index().plot()
plt.ylabel("Score")
plt.title("Attendance by Score")
plt.savefig('Attendencescore.png')
plt.show()