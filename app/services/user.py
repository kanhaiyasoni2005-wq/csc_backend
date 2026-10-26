from app.schemas.user import userSchema ,loginSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException, Request,status
from app.models.user import user
import jwt
from pwdlib import PasswordHash
from datetime import timedelta, datetime,timezone
from app.core.config import settings

encode = PasswordHash.recommended()
def varifyPassword(plainpassword, has_password):
    return encode.verify(plainpassword, has_password)

def user_create(data:userSchema,db:Session):
    has_password = encode.hash(data.password)
    new_user = user(
        name = data.name,
        phone = data.phone,
        email= data.email,
        password = has_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def user_login(data:loginSchema,db:Session):
    user1 = db.query(user).filter(user.email == data.email).first()
    if not user1:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= "wrong email id")
    if not varifyPassword(data.password, user1.password):
        raise HTTPException(status.HTTP_400_BAD_REQUEST,detail= "wrong email id and password")
    exp_time = datetime.now(timezone.utc)+timedelta(minutes=20)
    token = jwt.encode({"user_id": user1.id, "exp": exp_time},settings.SECRET_KEY,algorithm=settings.ALGORITHM )
    return token
def is_authentication(request:Request, db:Session):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)
   
    if not token.startswith("Bearer"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail= "token not start with bearer")
    extract_token = token.split(" ")[-1]
    if not extract_token:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="invalid token")
    userdata = jwt.decode(extract_token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
    user_id = userdata.get("user_id")
    # exp_time = userdata.get("exp")

    # current_time = datetime.timezone
    fatch_user = db.query(user).filter(user.id == user_id).first()
    return fatch_user