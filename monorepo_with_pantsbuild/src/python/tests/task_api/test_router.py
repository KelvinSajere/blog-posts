import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
from task_api.main import app  
from task_api.model import Task
import os
client = TestClient(app)


# Helper function to create a mock Task object
def create_mock_task(task_id, title, description):
    task = Task(id=task_id, title=title, description=description)
    task.to_dict = MagicMock(return_value={"id": task_id, "title": title, "description": description})
    return task

@pytest.fixture
def cleanup():
    yield
    if os.path.exists("tasks.db"):
        os.remove("tasks.db")



@patch("task_api.router.get_db")
@patch("task_api.router.create_task")
def test_add_task(mock_create_task, mock_get_db, cleanup):
    # Mock the database session and the create_task function
    db_session = MagicMock()
    mock_get_db.return_value = db_session

    # Setup a mock return value for create_task
    mock_task = create_mock_task(1, "Test Task", "Description")
    mock_create_task.return_value = mock_task

    response = client.post("/tasks",params={"title": "Test Task", "description": "Description"})
    
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Test Task", "description": "Description"}


@patch("task_api.router.get_db")
@patch("task_api.router.get_tasks")
def test_list_tasks(mock_get_tasks, mock_get_db, cleanup):
    # Mock the database session and the get_tasks function
    db_session = MagicMock()
    mock_get_db.return_value = db_session

    # Setup a mock return value for get_tasks
    mock_task = create_mock_task(1, "Test Task", "Description")
    mock_get_tasks.return_value = [mock_task]

    response = client.get("/tasks")
    
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "title": "Test Task", "description": "Description"}]


@patch("task_api.router.get_db")
@patch("task_api.router.update_task")
def test_edit_task(mock_update_task, mock_get_db, cleanup):
    # Mock the database session and the update_task function
    db_session = MagicMock()
    mock_get_db.return_value = db_session

    # Setup a mock return value for update_task
    mock_task = create_mock_task(1, "Updated Task", "Updated Description")
    mock_update_task.return_value = mock_task

    response = client.put("/tasks/1", params={"title": "Updated Task", "description": "Updated Description"})
    
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Updated Task", "description": "Updated Description"}

    # Test for a task not found (404)
    mock_update_task.return_value = None
    response = client.put("/tasks/999", params={"title": "Updated Task", "description": "Updated Description"})
    
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}


@patch("task_api.router.get_db")
@patch("task_api.router.delete_task")
def test_remove_task(mock_delete_task, mock_get_db, cleanup):
    # Mock the database session and the delete_task function
    db_session = MagicMock()
    mock_get_db.return_value = db_session

    response = client.delete("/tasks/1")
    
    assert response.status_code == 200
    assert response.json() == {"status": "Task deleted"}


def test_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "up"}
