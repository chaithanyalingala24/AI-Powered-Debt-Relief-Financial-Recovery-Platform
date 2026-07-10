from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models

from database import engine, get_db

from backend.schemas import (
    BorrowerCreate,
    LoanCreate,
    SettlementCreate,
    NegotiationHistoryCreate
)

from backend.service import (
    calculate_settlement,
    generate_letter,
    settlement_recommendation
)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Finance Backend API is running successfully!"}


# ---------------- BORROWERS ----------------

@app.post("/borrowers")
def create_borrower(
    borrower: BorrowerCreate,
    db: Session = Depends(get_db)
):

    new_borrower = models.Borrower(
        full_name=borrower.full_name,
        email=borrower.email,
        phone=borrower.phone
    )

    db.add(new_borrower)
    db.commit()
    db.refresh(new_borrower)

    return new_borrower


@app.get("/borrowers")
def get_borrowers(
    db: Session = Depends(get_db)
):

    return db.query(models.Borrower).all()


@app.get("/borrowers/{borrower_id}")
def get_borrower(
    borrower_id: int,
    db: Session = Depends(get_db)
):

    return db.query(
        models.Borrower
    ).filter(
        models.Borrower.id == borrower_id
    ).first()


# ---------------- LOANS ----------------

@app.post("/loans")
def create_loan(
    loan: LoanCreate,
    db: Session = Depends(get_db)
):

    new_loan = models.Loan(
        borrower_id=loan.borrower_id,
        lender_name=loan.lender_name,
        loan_type=loan.loan_type,
        loan_amount=loan.loan_amount,
        outstanding_amount=loan.outstanding_amount
    )

    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)

    return new_loan


@app.get("/loans")
def get_loans(
    db: Session = Depends(get_db)
):

    return db.query(models.Loan).all()


# ---------------- SETTLEMENTS ----------------

@app.post("/settlements")
def create_settlement(
    settlement: SettlementCreate,
    db: Session = Depends(get_db)
):

    new_settlement = models.Settlement(
        loan_id=settlement.loan_id,
        settlement_percentage=settlement.settlement_percentage,
        settlement_amount=settlement.settlement_amount
    )

    db.add(new_settlement)
    db.commit()
    db.refresh(new_settlement)

    return new_settlement


@app.get("/settlements")
def get_settlements(
    db: Session = Depends(get_db)
):

    return db.query(models.Settlement).all()


# ---------------- NEGOTIATIONS ----------------

@app.post("/negotiations")
def create_negotiation(
    negotiation: NegotiationHistoryCreate
):
    return {
        "message": "Negotiation history created",
        "data": negotiation
    }


# ---------------- STORY 2 APIs ----------------

@app.get("/calculate-settlement")
def settlement_calculator(
    outstanding_amount: int,
    percentage: int
):

    amount = calculate_settlement(
        outstanding_amount,
        percentage
    )

    return {
        "settlement_amount": amount
    }


@app.get("/validate-loan")
def validate(amount: int):

    if amount <= 0:
        return {
            "status": "Invalid Loan"
        }

    return {
        "status": "Valid Loan"
    }


@app.get("/recommend-settlement")
def recommendation(amount: int):

    percent = settlement_recommendation(amount)

    return {
        "recommended_percentage": percent
    }


@app.get("/generate-letter")
def letter(
    borrower: str,
    lender: str
):

    return {
        "letter": generate_letter(
            borrower,
            lender
        )
    }