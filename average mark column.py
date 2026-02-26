data["Average"] = data[["Math", "Science", "English"]].mean(axis=1)
print(data.head())