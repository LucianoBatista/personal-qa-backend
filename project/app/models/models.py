from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Table,
)
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    UserID = Column(Integer, primary_key=True)
    Username = Column(String(50), nullable=False)
    questions = relationship("Question", backref="user")


class Question(Base):
    __tablename__ = "questions"
    QuestionID = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey("users.UserID"), nullable=False)
    QuestionText = Column(String, nullable=False, unique=True)
    CreatedAt = Column(DateTime, nullable=False, default=datetime.now())
    UpdatedAt = Column(
        DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now()
    )
    answers = relationship("Answer", backref="question")
    tags = relationship("Tag", secondary="question_tags")


class Answer(Base):
    __tablename__ = "answers"
    AnswerID = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey("users.UserID"), nullable=False)
    QuestionID = Column(Integer, ForeignKey("questions.QuestionID"), nullable=False)
    AnswerText = Column(String, nullable=False, unique=True)
    CreatedAt = Column(DateTime, nullable=False, default=datetime.now())
    UpdatedAt = Column(
        DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now()
    )


class Tag(Base):
    __tablename__ = "tags"
    TagID = Column(Integer, primary_key=True)
    TagName = Column(String(50), nullable=False)
    CreatedAt = Column(DateTime, nullable=False, default=datetime.now())
    UpdatedAt = Column(
        DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now()
    )
    questions = relationship("Question", secondary="question_tags")


question_tags = Table(
    "question_tags",
    Base.metadata,
    Column("QuestionID", Integer, ForeignKey("questions.QuestionID")),
    Column("TagID", Integer, ForeignKey("tags.TagID")),
)
