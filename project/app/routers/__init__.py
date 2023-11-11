from fastapi import APIRouter

health_check_router = APIRouter(prefix="/health", tags=["Health"])
question_router = APIRouter(prefix="/questions", tags=["Questions"])
user_router = APIRouter(prefix="/users", tags=["Users"])
tag_router = APIRouter(prefix="/tags", tags=["Tags"])
# add other router here

# import others routers here
from . import health_check, questions, users, tags  # noqa: E402 F401
