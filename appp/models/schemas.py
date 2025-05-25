from pydantic import BaseModel
class Transaction(BaseModel):
    user_id:str
    amount:float
    txn_type:str
    timestamp:str