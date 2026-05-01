import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("student_data.xlsx")

print(data.head())
print(data.describe())

top_students = data.sort_values("Final_Marks", ascending=False)
print(top_students.head())

plt.scatter(data["Attendance (%)"], data["Final_Marks"])
plt.xlabel("Attendance (%)")
plt.ylabel("Final Marks")
plt.title("Attendance vs Final Marks")
plt.show()

plt.scatter(data["Study_Hours"], data["Final_Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.title("Study Hours vs Final Marks")
plt.show()
