from fastapi import status, Depends
from project.app.routers import user_router
from project.app.database.session import get_db_session
from sqlalchemy.orm import Session
from project.app.database.repository.user_crud import create_user_db


@user_router.post("", status_code=status.HTTP_200_OK)
def create_user(db: Session = Depends(get_db_session)):
    _ = create_user_db(db, "John")
    return {"Status": "ok"}
