import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task_api.database import Base
from task_api.model import Task

# Setup an in-memory SQLite database for testing
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def db():
    # Create tables in the in-memory database
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_task_model(db):
    # Create a Task instance
    task = Task(id=1, title="Test Task", description="This is a test description.")

    # Add the task to the session and commit
    db.add(task)
    db.commit()
    db.refresh(task)

    # Verify the Task instance was created correctly
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "This is a test description."

    # Test the to_dict method
    expected_dict = {
        "id": 1,
        "title": "Test Task",
        "description": "This is a test description.",
    }
    assert task.to_dict() == expected_dict
