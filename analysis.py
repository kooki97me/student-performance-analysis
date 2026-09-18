import pandas as pd
import matplotlib.pyplot as plt


# Load student data
data = pd.read_excel("student_data.xlsx")

# Display basic information
print("First five records:")
print(data.head())

print("\nDataset statistics:")
print(data.describe())

# Find top-performing students
top_students = data.sort_values(
    "Final_Marks",
    ascending=False
)

print("\nTop students:")
print(top_students.head())


# Attendance vs Final Marks
plt.figure(figsize=(8, 5))
plt.scatter(
    data["Attendance (%)"],
    data["Final_Marks"]
)
plt.xlabel("Attendance (%)")
plt.ylabel("Final Marks")
plt.title("Attendance vs Final Marks")
plt.grid(True)
plt.show()


# Study Hours vs Final Marks
plt.figure(figsize=(8, 5))
plt.scatter(
    data["Study_Hours"],
    data["Final_Marks"]
)
plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.title("Study Hours vs Final Marks")
plt.grid(True)
plt.show()
