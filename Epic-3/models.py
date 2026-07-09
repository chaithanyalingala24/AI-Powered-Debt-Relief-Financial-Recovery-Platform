from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Borrower(Base):
    __tablename__ = "borrowers"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)
    from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    borrower_id = Column(Integer, ForeignKey("borrowers.id"))
    lender_name = Column(String, nullable=False)
    loan_type = Column(String, nullable=False)
    loan_amount = Column(Integer, nullable=False)
    outstanding_amount = Column(Integer, nullable=False)

    borrower = relationship("Borrower")
class Settlement(Base):
    __tablename__ = "settlements"

    id = Column(Integer, primary_key=True, index=True)
    loan_id = Column(Integer, ForeignKey("loans.id"))
    settlement_percentage = Column(Integer, nullable=False)
    settlement_amount = Column(Integer, nullable=False)
    status = Column(String, default="Pending")

    loan = relationship("Loan")
class NegotiationHistory(Base):
    __tablename__ = "negotiation_history"

    id = Column(Integer, primary_key=True, index=True)
    settlement_id = Column(Integer, ForeignKey("settlements.id"))
    negotiation_letter = Column(String, nullable=False)
    negotiation_date = Column(String, nullable=False)

    settlement = relationship("Settlement")
