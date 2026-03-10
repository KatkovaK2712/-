from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    main_currency: Optional[str] = "RUB"


class UserCreate(UserBase):
    password: str

    @validator('password')
    def validate_password_length(cls, v):
        password_bytes = v.encode('utf-8')
        if len(password_bytes) > 72:
            raise ValueError('Пароль слишком длинный. Максимум 72 символа')
        if len(v) < 6:
            raise ValueError('Пароль слишком короткий. Минимум 6 символов')
        return v


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    main_currency: Optional[str] = None
    password: Optional[str] = None


class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True