from fastapi import APIRouter, HTTPException


from services.math_service import MathService
from services.user_service import UserService
from config.config import (
    get_redis_client,
    get_db_connection,
    return_db_connection
)
from models.models import (
    FactorialRequest,
    PowerRequest,
    FibbonaciRequest,
    AuthRequest,
    SignUpRequest
)


router = APIRouter()
math_service = MathService(get_redis_client)
user_service = UserService()


@router.post('/auth')
async def auth(req: AuthRequest):
    conn = await get_db_connection()
    try:
        user_exists = await user_service.handle_user_auth(
            conn=conn,
            email=req.email,
            password=req.password
        )
        if not user_exists:
            raise HTTPException(status_code=401, detail='Invalid credentials')
        return {'message': 'Login successful'}
    finally:
        await return_db_connection(conn)


@router.post('/sign-up')
async def sign_un(req: SignUpRequest):
    conn = await get_db_connection()
    try:
        success = await user_service.handle_user_sign_up(
            conn=conn,
            first_name=req.first_name,
            last_name=req.last_name,
            email=req.email,
            password=req.password,
            role=req.role
        )
        if not success:
            raise HTTPException(status_code=400,
                                detail='Failed to create user')
        return {'message': 'User registrated successfully'}
    finally:
        await return_db_connection(conn)


@router.post('/compute/factorial')
async def factorial(req: FactorialRequest):
    conn = await get_db_connection()
    try:
        result = await math_service.compute(conn,
                                            "factorial",
                                            number=req.number)
        return {"result": result}
    finally:
        await return_db_connection(conn)


@router.post("/compute/fibbonaci")
async def fibbonaci(req: FibbonaciRequest):
    conn = await get_db_connection()
    try:
        result = await math_service.compute(conn,
                                            "fibbonaci",
                                            number=req.number)
        return {"result": result}
    finally:
        await return_db_connection(conn)


@router.post("/compute/power")
async def power(req: PowerRequest):
    conn = await get_db_connection()
    try:
        result = await math_service.compute(conn,
                                            "power",
                                            base=req.base,
                                            exponent=req.exponent)
        return {"result": result}
    finally:
        await return_db_connection(conn)
