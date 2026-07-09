from pydantic import BaseModel

class BorrowerCreate(BaseModel):
    full_name: str
    email: str
    phone: str
class LoanCreate(BaseModel):
    borrower_id: int
    lender_name: str
    loan_type: str
    loan_amount: int
    outstanding_amount: int
class SettlementCreate(BaseModel):
    loan_id: int
    settlement_percentage: int
    settlement_amount: int
class NegotiationHistoryCreate(BaseModel):
    settlement_id: int
    negotiation_letter: str
    negotiation_date: str