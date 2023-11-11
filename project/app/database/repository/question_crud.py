from sqlalchemy.orm import Session
from project.app.models.models import Question
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
