from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Any

from app.db.database import get_db
from app.core.config import settings
from app.core.security import (
    verify_password,
    get_password_hash,
    create_access_token,
    get_current_user
)
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.schemas.token import Token

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(
        *,
        db: Session = Depends(get_db),
        user_in: UserCreate
) -> Any:
    """
    Регистрация нового пользователя
    """
    # Проверяем длину пароля (ограничение bcrypt - 72 байта)
    password_bytes = user_in.password.encode('utf-8')
    if len(password_bytes) > 72:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пароль слишком длинный. Максимальная длина - 72 символа"
        )

    if len(user_in.password) < 6:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пароль слишком короткий. Минимальная длина - 6 символов"
        )

    # Проверяем, не занят ли email
    user = db.query(User).filter(User.email == user_in.email).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с таким email уже существует"
        )

    # Создаём нового пользователя
    user = User(
        email=user_in.email,
        password_hash=get_password_hash(user_in.password),
        main_currency=user_in.main_currency
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@router.post("/login", response_model=Token)
def login(
        db: Session = Depends(get_db),
        form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    Вход в систему (получение JWT-токена)
    """
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный email или пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный email или пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserResponse)
def read_users_me(
        current_user: User = Depends(get_current_user)
) -> Any:
    """
    Получить информацию о текущем пользователе
    """
    return current_user