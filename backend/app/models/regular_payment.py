from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Enum, Text, Boolean
from sqlalchemy.orm import relationship
from ..db.database import Base
import enum

class PaymentFrequency(str, enum.Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"

class RegularPayment(Base):
    __tablename__ = "regular_payments"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    account_id = Column(Integer, ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="SET NULL"), nullable=True)
    
    name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    frequency = Column(Enum(PaymentFrequency), nullable=False)
    day_of_month = Column(Integer, nullable=True)  # для ежемесячных
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)  # Теперь Boolean импортирован!
    
    # Связи
    user = relationship("User", back_populates="regular_payments")
    account = relationship("Account")
    category = relationship("Category")