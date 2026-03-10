from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from ..db.database import Base
import enum
import datetime

class BudgetPeriod(str, enum.Enum):
    MONTHLY = "monthly"
    YEARLY = "yearly"

class Budget(Base):
    __tablename__ = "budgets"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    
    amount_limit = Column(Float, nullable=False)
    period = Column(Enum(BudgetPeriod), default=BudgetPeriod.MONTHLY)
    start_date = Column(Date, default=datetime.date.today)
    
    # Связи
    user = relationship("User", back_populates="budgets")
    category = relationship("Category")