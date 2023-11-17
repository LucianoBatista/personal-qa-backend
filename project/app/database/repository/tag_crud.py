from sqlalchemy.orm import Session
from project.app.models.models import Tag, question_tags


def create_tag_db(db: Session, tags: list[str]) -> list[Tag] | list:
    """
    Create tags in database only if they do not exist
    """
    # find existing tags
    existing_tags = db.query(Tag).distinct(Tag.TagName).all()
    existing_tags = [tag.TagName for tag in existing_tags]

    # remove existing_tags from tags
    tags = list(set(tags) - set(existing_tags))

    if len(tags) == 0:
        return []
    else:
        tags = [
            Tag(
                TagName=tag_text,
            )
            for tag_text in tags
        ]

        db.add_all(tags)
        db.commit()

        return tags


def append_tag_db(db: Session, question_id: int, tag_ids: list[int]) -> None:
    for tag_id in tag_ids:
        db.execute(question_tags.insert().values(QuestionID=question_id, TagID=tag_id))
        db.commit()


def get_all_tags_db(db: Session) -> list[str]:
    tags = db.query(Tag).all()
    tags = [str(tag.TagName) for tag in tags]
    return tags
