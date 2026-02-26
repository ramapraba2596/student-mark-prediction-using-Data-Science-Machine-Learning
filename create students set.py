np.random.seed(42)

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