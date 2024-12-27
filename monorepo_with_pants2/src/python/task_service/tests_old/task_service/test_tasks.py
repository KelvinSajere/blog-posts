def test_create_task(client):
    response = client.post(f"/tasks?title=Test Task&description=Test description")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"


def test_list_tasks(client):
    response = client.get("/tasks/")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 0
