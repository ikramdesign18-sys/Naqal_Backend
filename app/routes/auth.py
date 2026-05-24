from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.supabase_client import supabase

router = APIRouter()

class UserCreate(BaseModel):
    email: str
    password: str

@router.post("/signup")
async def signup(user: UserCreate):
    try:
        response = supabase.auth.sign_up({
            "email": user.email,
            "password": user.password
        })
        return {"status": "success", "user": response.user}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
async def login(user: UserCreate):
    try:
        response = supabase.auth.sign_in_with_password({
            "email": user.email,
            "password": user.password
        })
        return {"status": "success", "token": response.session.access_token}
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid credentials")