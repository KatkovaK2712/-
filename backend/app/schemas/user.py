from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Базовая схема (общие поля)
class UserBase(BaseModel):
    email: EmailStr
    main_currency: Optional[str] = "RUB"

# Для создания пользователя (регистрация)
class UserCreate(UserBase):
    password: str

# Для ответа (то, что отдаем клиенту)
class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True  # для работы с SQLAlchemy моделями

# Для обновления
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    main_currency: Optional[str] = None