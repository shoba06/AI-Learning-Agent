import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

data = pd.read_csv("learning_data.csv")

X = data[["watches_videos", "prefers_audio", "likes_practical", "reads_notes"]]
y = data["learning_style"]

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained successfully!")
