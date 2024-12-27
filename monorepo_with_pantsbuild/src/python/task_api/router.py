from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from task_api.database import get_db
from task_api.service import create_task, delete_task, get_tasks, update_task

router = APIRouter()


@router.post("/tasks")
def add_task(title: str, description: str, db: Session = Depends(get_db)):
    task = create_task(db, title, description)
    return task.to_dict()


@router.get("/tasks")
def list_tasks(db: Session = Depends(get_db)):
    tasks = get_tasks(db)
    return [task.to_dict() for task in tasks]


@router.put("/tasks/{task_id}")
def edit_task(
    task_id: int, title: str, description: str, db: Session = Depends(get_db)
):
    task = update_task(db, task_id, title, description)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task.to_dict()


@router.delete("/tasks/{task_id}")
def remove_task(task_id: int, db: Session = Depends(get_db)):
    delete_task(db, task_id)
    return {"status": "Task deleted"}


@router.get("/")
def health():
    return {"status": "up"}
