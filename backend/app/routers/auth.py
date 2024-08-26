from fastapi import APIRouter, Depends
from app.auth import verify_token


router = APIRouter(dependencies=[Depends(verify_token)])


@router.get("/")
def verify_jwt():
    return {"message": "success"}
