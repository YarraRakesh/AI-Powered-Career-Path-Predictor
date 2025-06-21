import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

print("🔍 Reading dataset...")
df = pd.read_csv("career_data.csv")  # use the new expanded file

X = df.drop("Career", axis=1)
y = df["Career"]

print("🔧 Encoding labels...")
le = LabelEncoder()
y_encoded = le.fit_transform(y)

print("🚀 Training model...")
model = RandomForestClassifier()
model.fit(X, y_encoded)

print("💾 Saving model to model.pkl...")
with open("model.pkl", "wb") as f:
    pickle.dump((model, le), f)

print("✅ Model trained and saved successfully.")
