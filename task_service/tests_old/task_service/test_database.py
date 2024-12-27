from task_service.database import get_db
from tests.task_service.conftest import TestingSessionLocal


def test_get_db(client):
    """Test the get_db function."""
    db = next(get_db())
    assert db is not None
