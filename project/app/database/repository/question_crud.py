from sqlalchemy.orm import Session
from project.app.models.models import Question, Answer, question_tags, Tag
from datetime import datetime


def create_question_db(db: Session, question_text: str, user_id: int) -> Question:
    question = Question(
        UserID=user_id,
        QuestionText=question_text,
    )

    db.add(question)
    db.commit()
    db.refresh(question)
    db.close()
    return question


def get_question_db(db: Session, id: int) -> Question:
    question = db.query(Question).filter(Question.QuestionID == id).first()
    return question


def get_answer_db(db: Session, id: int) -> Answer:
    answer = db.query(Answer).filter(Answer.QuestionID == id).first()
    return answer


def append_answer_db(db: Session, answer_text: str, question_id: int) -> None:
    answer = Answer(
        UserID=1,
        QuestionID=question_id,
        AnswerText=answer_text,
    )
    db.add(answer)
    db.commit()
    db.refresh(answer)


def put_question_ans_db(
    db: Session, question_id: int, question_text: str, answer_text: str
) -> None:
    # Update records directly
    db.query(Question).filter(Question.QuestionID == question_id).update(
        {Question.QuestionText: question_text},
        synchronize_session=False,
    )

    db.query(Answer).filter(Answer.QuestionID == question_id).update(
        {Answer.AnswerText: answer_text},
        synchronize_session=False,
    )

    db.commit()


def get_question_by_tag_db(db: Session, tags: list[str], n_question: int) -> list:
    # get tags ids
    tags = db.query(Tag.TagID).filter(Tag.TagName.in_(tags)).all()
    tags_items = [tag[0] for tag in tags]

    # get question ids
    question_ids = (
        db.query(question_tags.c.QuestionID)
        .filter(question_tags.c.TagID.in_(tags_items))
        .all()
    )
    question_ids = [question_id[0] for question_id in question_ids]
    question_ids = list(set(question_ids))

    # merge questions and answers
    query = (
        db.query(Question, Answer)
        .outerjoin(Answer, Question.QuestionID == Answer.QuestionID)
        .filter(Question.QuestionID.in_(question_ids))
    )
    objs = query.all()

    question_and_answers = []
    for question, answer in objs:
        if answer is None:
            answer_ = ""
        else:
            answer_ = answer.AnswerText
        question_and_answers.append((question.QuestionText, answer_))

    # format to output
    questions = [
        {"question": question, "answer": answer}
        for question, answer in question_and_answers
    ]

    return questions
