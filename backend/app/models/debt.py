from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..db.database import Base
import enum

class DebtType(str, enum.Enum):
    I_OWE = "i_owe"        # я должен
    OWE_ME = "owe_me"      # должны мне
    CREDIT = "credit"      # кредит в банке

class DebtStatus(str, enum.Enum):
    ACTIVE = "active"
    CLOSED = "closed"

class Debt(Base):
    __tablename__ = "debts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    type = Column(Enum(DebtType), nullable=False)
    counterparty = Column(String, nullable=False)  # кому/от кого
    amount = Column(Float, nullable=False)
    interest_rate = Column(Float, default=0.0)  # годовая ставка
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    payment_amount = Column(Float, nullable=True)  # ежемесячный платеж
    description = Column(Text, nullable=True)
    status = Column(Enum(DebtStatus), default=DebtStatus.ACTIVE)
    
    # Связи
    user = relationship("User", back_populates="debts")