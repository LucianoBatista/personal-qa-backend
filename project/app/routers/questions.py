from fastapi import status, Depends
from project.app.routers import question_router
from project.app.database.session import get_db_session
from sqlalchemy.orm import Session
from project.app.database.repository.question_crud import (
    create_question_db,
    append_answer_db,
)


@question_router.post("/create_question", status_code=status.HTTP_200_OK)
def create_question(db: Session = Depends(get_db_session)):
    _ = create_question_db(db, "How to create a question?")
    return {"Status": "ok"}


@question_router.post("/append_answer", status_code=status.HTTP_200_OK)
def append_answer(db: Session = Depends(get_db_session)):
    _ = append_answer_db(db, "This is my answer")
    return {"Status": "ok"}
