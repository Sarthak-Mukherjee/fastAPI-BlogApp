from fastapi import APIRouter, HTTPException, status, Depends, Response, FastAPI
from .. import models, schemas, utils, oauth2
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(tags = ["Authentication"])

@router.post("/login")
def user_login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()

    if not user:
        raise HTTPException(status_code  = status.HTTP_404_NOT_FOUND, detail = "Invalid credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    
    access_token = oauth2.create_acces_token(data = {"user_id": user.id})
    return {"acces_token" : access_token, "token_type" : "bearer"}


