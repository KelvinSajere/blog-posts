from task_service.model import Task


def test_task_model(db_session):
    """Test creating a Task model instance."""
    new_task = Task(title="Test Task", description="Test Description")
    db_session.add(new_task)
    db_session.commit()
    db_session.refresh(new_task)

    assert new_task.id is not None  # Check that the ID is set after commit
    assert new_task.title == "Test Task"
    assert new_task.description == "Test Description"
