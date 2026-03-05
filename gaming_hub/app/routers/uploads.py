from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlmodel import Session
import shutil
import os
from ..database import get_session
from ..models import User

router = APIRouter(prefix="/uploads", tags=["Uploads"])

UPLOAD_DIR = "app/static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/avatar/{user_id}")
async def upload_avatar(user_id: int, file: UploadFile = File(...), session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    
    # Actualizamos la URL del avatar en la base de datos
    user.avatar_url = f"/static/uploads/{file.filename}"
    session.add(user)
    session.commit()
    session.refresh(user)
    
    return {"info": f"Archivo '{file.filename}' guardado", "url": user.avatar_url}