from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TransactionBase(BaseModel):
    account_id: int
    category_id: Optional[int] = None
    amount: float
    type: Literal["income", "expense", "transfer"]
    description: Optional[str] = None
    to_account_id: Optional[int] = None

class TransactionCreate(TransactionBase):
    # Специальное поле для суммирования (пользователь может ввести "10+20+5")
    amount_raw: Optional[str] = None
    date: Optional[datetime] = None

class TransactionUpdate(BaseModel):
    amount: Optional[float] = None
    category_id: Optional[int] = None
    account_id: Optional[int] = None
    description: Optional[str] = None

class TransactionResponse(TransactionBase):
    id: int
    user_id: int
    date: datetime
    
    class Config:
        from_attributes = True