def score_transaction(txn):
    if txn.amount>10000 and txn.txn_type.lower()=='international':
        return 0.9, "High-risk transaction due to large amount and international type"
    return 0.1, "Low-risk transaction"