from fastapi import FastAPI
from appp.routes import transaction, compliance
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


app = FastAPI()

# For debug
print("Transaction route loaded:", transaction.router)
print("Compliance route loaded:", compliance.router)

# Register the routers
app.include_router(transaction.router)
app.include_router(compliance.router)

@app.get("/")
def root():
    return {"message": "GenAI Banking app"}
