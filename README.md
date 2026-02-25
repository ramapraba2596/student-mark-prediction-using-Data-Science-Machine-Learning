# student-mark-prediction-using-Data-Science-Machine-Learning
This project predicts a student’s marks based on their study hours and attendance percentage using a Simple Linear Regression model.
Libraries used: pandas for data handling, numpy for creating random data, and scikit-learn for training the model and evaluating it.
Dataset: Randomly generated 30 samples with Study_Hours, Attendance, and Marks. (np.random.seed(42) used for reproducibility)
Features:
Study_Hours → Number of hours studied per day
Attendance → Percentage of classes attended
Target: Marks → Predicted marks of the student
Process:
Import libraries and create dataset
Split data into train and test sets
Train Linear Regression model
Predict marks on test set and evaluate with R² score
Take new input from user to predict marks interactively
