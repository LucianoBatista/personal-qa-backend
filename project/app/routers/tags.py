from fastapi import status, Depends
from project.app.routers import tag_router
from project.app.database.session import get_db_session
from sqlalchemy.orm import Session
from project.app.database.repository.tag_crud import (
    create_tag_db,
    get_all_tags_db,
)  # append_tag_db


@tag_router.post("/create_tag", status_code=status.HTTP_200_OK)
def create_tag(db: Session = Depends(get_db_session)):
    _ = create_tag_db(db, ["AI Learning"])
    return {"Status": "ok"}


@tag_router.get("/get_all", status_code=status.HTTP_200_OK)
def get_all_tags(db: Session = Depends(get_db_session)):
    tags = get_all_tags_db(db)
    return tags


# @tag_router.post("/append_tag", status_code=status.HTTP_200_OK)
# def append_tag(db: Session = Depends(get_db_session)):
#     _ = append_tag_db(db, 1, 1)
#     return {"Status": "ok"}
