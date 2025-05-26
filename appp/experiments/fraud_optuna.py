from pathlib import Path
import optuna, mlflow, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from joblib import dump

# ───────── Paths ─────────
ROOT = Path(__file__).resolve().parents[2]
DATA_PATH  = ROOT / "Dataset" / "transactions.csv"
MODEL_PATH = ROOT / "model.pkl"

# ───────── Data ──────────
df = pd.read_csv(DATA_PATH)
FEATURES = ["amount", "txn_type", "location", "device_type"]
X = df[FEATURES]
y = df["is_fraud"]

cat_cols = ["txn_type", "location", "device_type"]
num_cols = ["amount"]

preprocess = ColumnTransformer(
    [("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
     ("num", "passthrough",                     num_cols)]
)

X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42
)

# ───────── MLflow ─────────
mlflow.set_tracking_uri("http://localhost:5001")   # change if inside a container
mlflow.set_experiment("Fraud Detection Optuna")

def objective(trial):
    params = {
        "n_estimators":      trial.suggest_int("n_estimators", 50, 300),
        "max_depth":         trial.suggest_int("max_depth", 3, 20),
        "min_samples_split": trial.suggest_int("min_samples_split", 2, 10),
        "min_samples_leaf":  trial.suggest_int("min_samples_leaf", 1, 4),
    }

    with mlflow.start_run(nested=True):
        clf = make_pipeline(
            preprocess,
            RandomForestClassifier(**params, random_state=42, n_jobs=-1)
        )
        clf.fit(X_tr, y_tr)
        auc = roc_auc_score(y_te, clf.predict_proba(X_te)[:, 1])

        mlflow.log_params(params)
        mlflow.log_metric("auc", auc)

    return auc

# ───────── Search ─────────
if __name__ == "__main__":
    study = optuna.create_study(direction="maximize")
    study.optimize(objective, n_trials=25, show_progress_bar=True)

    best_params = study.best_params
    print("🏆 Best params:", best_params)

    final_model = make_pipeline(
        preprocess,
        RandomForestClassifier(**best_params, random_state=42, n_jobs=-1)
    )
    final_model.fit(X_tr, y_tr)
    dump(final_model, MODEL_PATH)
    print(f"✅ Final model saved at {MODEL_PATH}")
