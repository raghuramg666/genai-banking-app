from fastapi import APIRouter
from pydantic import BaseModel
from appp.services.rag_engine import query_compliance

router = APIRouter()

class QARequest(BaseModel):
    question: str

@router.post("/compliance-qa")
def compliance_qa(req: QARequest):
    return {"answer": query_compliance(req.question)}
