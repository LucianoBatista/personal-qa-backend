from sqlalchemy.orm import Session
from project.app.models.models import Question, Answer
from datetime import datetime


def create_question_db(db: Session, question_text: str) -> None:
    question = Question(
        UserID=1,
        QuestionText=question_text,
        DateAsked=datetime.now(),
    )

    db.add(question)
    db.commit()
    db.refresh(question)
    db.close()


def append_answer_db(db: Session, answer_text: str) -> None:
    answer = Answer(
        UserID=1,
        QuestionID=1,
        AnswerText=answer_text,
        DateAnswered=datetime.now(),
    )
    db.add(answer)
    db.commit()
    db.refresh(answer)
    db.close()
