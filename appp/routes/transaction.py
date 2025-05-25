from fastapi import APIRouter
from appp.models.schemas import Transaction
from appp.services.risk_engine import score_transaction

router = APIRouter()

@router.post("/txn")
def analyze_transaction(txn: Transaction):
    score, reason = score_transaction(txn)
    return {"score": score, "reason": reason}
