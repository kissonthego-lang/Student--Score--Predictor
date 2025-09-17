import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("dataset.csv")
X = data[["Hours"]]   # Feature (Study Hours)
y = data["Score"]     # Target (Exam Score)

# Train model
model = LinearRegression()
model.fit(X, y)

print("📊 Student Score Predictor")
print("----------------------------")

# Take input from user
try:
    hours = float(input("Enter number of study hours: "))
    predicted_score = model.predict([[hours]])
    print(f"Predicted Exam Score for {hours} study hours = {predicted_score[0]:.2f}")
except:
    print("⚠️ Please enter a valid number.")
