from sqlalchemy.orm import Session
from project.app.models.models import Tag, question_tags


def create_tag_db(db: Session, tag_text: str) -> None:
    question = Tag(
        TagName=tag_text,
    )

    db.add(question)
    db.commit()
    db.refresh(question)
    db.close()


def append_tag_db(db: Session, question_id: int, tag_id: int) -> None:
    db.execute(question_tags.insert().values(QuestionID=question_id, TagID=tag_id))
    db.commit()
    db.close()
