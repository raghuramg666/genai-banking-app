from fastapi import FastAPI
from appp.routes import transaction, compliance
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


app = FastAPI()



# Register the routers
app.include_router(transaction.router)
app.include_router(compliance.router)

@app.get("/")
def root():
    return {"message": "GenAI Banking app"}
