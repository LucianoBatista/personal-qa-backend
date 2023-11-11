from sqlalchemy.orm import Session
from project.app.models.models import User


def create_user_db(db: Session, user_name: str) -> None:
    user = User(
        Username=user_name,
        Email="test@gotmmail.com",
        Password="123456",
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
