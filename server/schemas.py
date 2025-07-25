from pydantic import BaseModel, Field
from typing import Optional

class FactorialRequest(BaseModel):
    number: int = Field(..., ge=0)

class PowerRequest(BaseModel):
    number: float
    power: int

class FibbonaciRequest(BaseModel):
    number: int = Field(..., ge=1)
