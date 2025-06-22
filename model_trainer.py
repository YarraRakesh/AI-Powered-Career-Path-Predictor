import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle

print("🔍 Reading dataset...")
df = pd.read_csv("career_data.csv")  # Make sure this file is present

# 🎯 Drop rows with missing values (if any)
df.dropna(inplace=True)

print("🔧 Encoding target labels...")
le = LabelEncoder()
df['Career_Label'] = le.fit_transform(df['Career'])

# Feature columns used in the app
feature_cols = [
    "Math", "English", "Coding", "Loves_Tech", "Loves_Design",
    "Talks_Alot", "Logic", "Likes_Outdoor", "Research_Interest",
    "Work_Env", "Learning_Style", "Knows_Python", "Knows_C",
    "Knows_CPP", "Knows_Java", "Team_Player", "Leadership_Score",
    "Adaptability_Score", "Interested_in_AI", "Interested_in_Blockchain",
    "Interested_in_Cybersecurity", "Interested_in_VLSI", "Interested_in_Robotics"
]

X = df[feature_cols]
y = df['Career_Label']

# 🔄 Split dataset
print("📊 Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🚀 Train model
print("🧠 Training model...")
model = RandomForestClassifier(n_estimators=150, random_state=42)
model.fit(X_train, y_train)

# 💾 Save model and label encoder
print("💾 Saving model and label encoder...")
with open("model.pkl", "wb") as f:
    pickle.dump((model, le), f)

print("✅ Model training complete!")