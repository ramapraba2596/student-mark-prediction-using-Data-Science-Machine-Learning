import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Random Seed (same output varanum)
np.random.seed(42)

# Step 2: Create Dataset (30 Students)
data = pd.DataFrame({
    "Student_ID": range(1, 31),
    "Class": np.random.choice(["10A", "10B", "10C"], 30),
    "Gender": np.random.choice(["Male", "Female"], 30),
    "Math": np.random.randint(40, 100, 30),
    "Science": np.random.randint(45, 100, 30),
    "English": np.random.randint(50, 100, 30),
    "Study_Hours": np.random.randint(1, 6, 30),
    "Attendance_%": np.random.randint(60, 100, 30)
})

# Step 3: Add Average Column
data["Average"] = data[["Math", "Science", "English"]].mean(axis=1)

print("First 5 Records:\n")
print(data.head())

# Step 4: Subject-wise Average
print("\nSubject-wise Average:")
subject_avg = data[["Math", "Science", "English"]].mean()
print(subject_avg)

# Step 5: Study Hours vs Average Correlation
print("\nStudy Hours vs Average Correlation:")
print(data[["Study_Hours", "Average"]].corr())

# Step 6: Class-wise Performance
print("\nClass-wise Average Performance:")
print(data.groupby("Class")["Average"].mean())

# Step 7: Attendance Impact
print("\nAttendance vs Average Correlation:")
print(data[["Attendance_%", "Average"]].corr())

# Step 8: Top 5 Students
print("\nTop 5 Students:")
print(data.sort_values(by="Average", ascending=False).head(5))

# ---------------- VISUALIZATION ----------------

# Subject Performance
plt.figure()
subject_avg.plot(kind="bar")
plt.title("Average Marks per Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()

# Class Performance
plt.figure()
data.groupby("Class")["Average"].mean().plot(kind="bar")
plt.title("Class-wise Average Performance")
plt.xlabel("Class")
plt.ylabel("Average Marks")
plt.show()

# Study Hours vs Performance
plt.figure()
plt.scatter(data["Study_Hours"], data["Average"])
plt.xlabel("Study Hours")
plt.ylabel("Average Marks")
plt.title("Study Hours vs Performance")
plt.show()
