from sqlalchemy.orm import Session
from task_api.model import Task


def create_task(db: Session, title: str, description: str):
    task = Task(title=title, description=description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task









def get_tasks(db: Session):
    return db.query(Task).all()


def update_task(db: Session, task_id: int, title: str, description: str):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.title = title
        task.description = description
        db.commit()
        db.refresh(task)
        return task
    return None


def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
