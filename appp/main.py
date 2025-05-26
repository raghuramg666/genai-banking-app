from fastapi import FastAPI
from appp.routes import transaction, compliance
from dotenv import load_dotenv
from appp.routes import shap_explainer
from prometheus_fastapi_instrumentator import Instrumentator





import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


app = FastAPI()

Instrumentator().instrument(app).expose(app)

# Register the routers
app.include_router(transaction.router)
app.include_router(compliance.router)
app.include_router(shap_explainer.router)

@app.get("/")
def root():
    return {"message": "GenAI Banking app"}
