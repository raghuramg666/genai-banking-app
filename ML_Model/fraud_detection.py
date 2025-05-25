
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
import joblib

# Get the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Define the path to the CSV
DATA_PATH = BASE_DIR/"Dataset"/"transactions.csv"
print(DATA_PATH)
# Load the data
df = pd.read_csv(DATA_PATH)




# Features & target
X = df[["amount", "txn_type", "location", "device_type"]]
y = df["is_fraud"]

# Preprocessing
categorical = ["txn_type", "location", "device_type"]
numeric = ["amount"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
        ("num", "passthrough", numeric)
    ]
)

# Model pipeline
model = make_pipeline(preprocessor, RandomForestClassifier(n_estimators=100, random_state=42))

# Train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")
print("✅ model.pkl saved.")
