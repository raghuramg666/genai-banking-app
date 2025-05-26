# 🏦 GenAI Banking Compliance & Risk Assistant

A production-grade, zero-cost regulatory tech project built with **FastAPI**, **Streamlit**, **MLflow**, **FAISS**, **Groq LLM**, **SHAP**, **Docker Compose**, and **Grafana** — demonstrating deep skills across **machine learning, retrieval-augmented generation, MLOps, and observability**.

---

## 🔥 Key Highlights

- ✅ Real-time fraud risk scoring using ML model (RandomForest)
- ✅ SHAP-based explainability (`/fraud_explain`)
- ✅ Compliance Q&A over uploaded policy PDFs (RAG using FAISS + Groq)
- ✅ Upload support for new documents via Streamlit + FastAPI
- ✅ Prometheus + Grafana observability dashboard
- ✅ Tracked experiments via MLflow
- ✅ Containerized with Docker Compose for local orchestration

---

## 🚀 Tech Stack

| Domain         | Tools / Frameworks                                      |
|----------------|---------------------------------------------------------|
| Backend        | FastAPI, Uvicorn                                        |
| Frontend       | Streamlit                                               |
| ML & Explain   | Scikit-learn, SHAP, Optuna (planned), MLflow            |
| GenAI & RAG    | FAISS, SentenceTransformers, pdfplumber, Groq API       |
| Observability  | Prometheus, Grafana, prometheus-fastapi-instrumentator |
| Orchestration  | Docker, Docker Compose                                  |

---

## 🧠 Core Features

### 📈 Fraud Transaction Risk Analysis (`/txn`)
- Input: `amount`, `txn_type`, `location`, `device_type`
- ML model (RandomForest) returns fraud **risk score** and reason
- SHAP visualization via `/fraud_explain` for transparency

### 📄 Compliance Q&A with RAG (`/compliance-qa`)
- Upload PDFs (AML/KYC/etc.)
- Documents embedded with `sentence-transformers` and stored in FAISS
- Questions are answered using Groq-hosted LLM with retrieved context

### ⚙️ MLFlow Tracking
- ML experiments are logged to `mlflow.db`
- View via: [http://localhost:5001](http://localhost:5001)

### 📊 Observability
- FastAPI metrics exposed to Prometheus
- Dashboards available at: [http://localhost:3000](http://localhost:3000)

---

## 🖼️ Streamlit UI

```bash
streamlit run app_ui.py
