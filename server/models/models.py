from pydantic import BaseModel, Field
from typing import Optional


class FactorialRequest(BaseModel):
    number: int = Field(..., ge=0)


class PowerRequest(BaseModel):
    base: float
    exponent: int


class FibbonaciRequest(BaseModel):
    number: int = Field(..., ge=1)


class AuthRequest(BaseModel):
    email: str
    password: str


class SignUpRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    role: Optional[str] = None
