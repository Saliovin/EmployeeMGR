import app.schemas.user as schemas
import app.crud.user as crud
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.auth import is_pass_valid, generate_jwt
from app.database import get_db

router = APIRouter()


@router.post("/login/")
def login_user(
    response: Response, user: schemas.UserLogin, db: Session = Depends(get_db)
):
    db_user = crud.get_user(db, username=user.username)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Invalid login credentials")
    if is_pass_valid(user.password.encode(), db_user.hashed_password):
        token = generate_jwt(user.username)
        response.set_cookie(key="token", value=token, httponly=True)
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=400, detail="Invalid login credentials")


@router.post("/logout/")
def logout_user(response: Response):
    response.delete_cookie(key="token")
    return {"message": "Logout successful"}
