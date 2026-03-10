from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime

class AccountBase(BaseModel):
    name: str
    type: Literal["card", "cash", "savings", "credit"]
    currency: str = "RUB"
    interest_rate: Optional[float] = 0.0
    min_balance: Optional[float] = 0.0
    credit_limit: Optional[float] = 0.0
    payment_date: Optional[int] = None

class AccountCreate(AccountBase):
    initial_balance: float = 0.0

class AccountUpdate(BaseModel):
    name: Optional[str] = None
    balance: Optional[float] = None

class AccountResponse(AccountBase):
    id: int
    user_id: int
    balance: float
    created_at: datetime
    
    class Config:
        from_attributes = True