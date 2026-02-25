np.random.seed(42)

data = pd.DataFrame({
    "Study_Hours": np.random.randint(1, 7, 30),
    "Attendance": np.random.randint(60, 100, 30),
    "Marks": np.random.randint(40, 100, 30)
})

data.head()