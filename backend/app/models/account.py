from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..db.database import Base
import enum

class AccountType(str, enum.Enum):
    CARD = "card"           # банковская карта
    CASH = "cash"           # наличные
    SAVINGS = "savings"     # накопительный счет
    CREDIT = "credit"       # кредит

class Account(Base):
    __tablename__ = "accounts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)
    type = Column(Enum(AccountType), nullable=False)
    balance = Column(Float, default=0.0)
    currency = Column(String, default="RUB")
    
    # Для накопительных счетов
    interest_rate = Column(Float, default=0.0)  # годовая ставка в %
    min_balance = Column(Float, default=0.0)    # минимальный остаток для начисления
    
    # Для кредитов
    credit_limit = Column(Float, default=0.0)
    payment_date = Column(Integer, nullable=True)  # день месяца платежа
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Связи
    user = relationship("User", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")