from typing import Optional
from fastapi import status, Depends
from sqlalchemy.exc import IntegrityError
from project.app.routers import question_router
from project.app.database.session import get_db_session
from sqlalchemy.orm import Session
from project.app.database.repository.question_crud import (
    create_question_db,
    append_answer_db,
    get_question_db,
    get_answer_db,
    append_answer_db,
    put_question_ans_db,
    get_question_by_tag_db,
)
from project.app.database.repository.tag_crud import create_tag_db, append_tag_db
from pydantic import BaseModel
from starlette.status import HTTP_400_BAD_REQUEST
from fastapi.exceptions import HTTPException
import numpy as np


class QuestionInput(BaseModel):
    user_id: int
    question_text: str
    question_tags: list[str]
    answer_text: Optional[str] = ""


class AnswerInput(BaseModel):
    user_id: int
    question_id: int
    answer_text: str


class QuestionUpdateInput(BaseModel):
    question_id: int
    question_text: str
    answer_text: str


class ByTagInput(BaseModel):
    tag: list[str]
    n_question: int


@question_router.post("/create_question", status_code=status.HTTP_200_OK)
def create_question(
    question_data: QuestionInput,
    db: Session = Depends(get_db_session),
):
    # retrieve data from request
    user_id = question_data.user_id
    question_text = question_data.question_text
    question_tags = question_data.question_tags
    answer_text = question_data.answer_text

    try:
        question = create_question_db(db, question_text, user_id)
        tags = create_tag_db(db, question_tags)
        _ = append_answer_db(db, answer_text, question.QuestionID)
        _ = append_tag_db(db, question.QuestionID, [tag.TagID for tag in tags])
    except IntegrityError as e:
        print(e)
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Could not create question.",
        )

    return {"question_id": question.QuestionID}


@question_router.post("/append_answer", status_code=status.HTTP_200_OK)
def append_answer(answer: AnswerInput, db: Session = Depends(get_db_session)):
    _ = answer.user_id
    question_id = answer.question_id
    answer_text = answer.answer_text

    _ = append_answer_db(db, answer_text, question_id)
    return {"Status": "ok"}


@question_router.get("/get_question", status_code=status.HTTP_200_OK)
def get_question(id: int, db: Session = Depends(get_db_session)):
    try:
        question = get_question_db(db, id)
        answer = get_answer_db(db, id)
    except:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Could not find this question.",
        )

    if question is None:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Could not find this question.",
        )

    if answer is None:
        return {"question": question.QuestionText, "answer": ""}
    return {"question": question.QuestionText, "answer": answer.AnswerText}


@question_router.put("/put_question", status_code=status.HTTP_200_OK)
def put_question(
    question_update: QuestionUpdateInput, db: Session = Depends(get_db_session)
):
    id = question_update.question_id
    question_text = question_update.question_text
    answer_text = question_update.answer_text

    _ = put_question_ans_db(db, id, question_text, answer_text)
    return {"Status": "ok"}


@question_router.post("/by_tag", status_code=status.HTTP_200_OK)
def get_question_by_tag(params: ByTagInput, db: Session = Depends(get_db_session)):
    tag = params.tag
    n_question = params.n_question

    questions = get_question_by_tag_db(db, tag, n_question)

    # probably not the best way to do this
    np.random.shuffle(questions)
    questions = questions[:n_question]
    return questions
