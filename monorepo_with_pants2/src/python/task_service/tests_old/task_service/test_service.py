from sqlalchemy import text
from task_service.service import create_task, get_tasks


def test_create_task_service(db_session):
    """Test the create_task service function."""
    task_data = {"title": "New Task", "description": "New Task Description"}
    task = create_task(db=db_session, **task_data)

    result = list(db_session.execute(text("Select * from tasks")))[0]

    assert task.id is not None  # Check that the ID is set
    assert task.title == "New Task"
    assert task.description == "New Task Description"

    assert result[0] == 1
    assert result[1] == "New Task"
    # assert result[2] == "New Task Description"


def test_get_tasks_service(db_session):
    """Test the get_tasks service function."""
    create_task(db_session, **{"title": "Task 1", "description": "Description 1"})
    create_task(db_session, **{"title": "Task 2", "description": "Description 2"})

    tasks = get_tasks(db_session)
    assert len(tasks) == 2  # Check the number of tasks retrieved
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"
