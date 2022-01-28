import pytest
from employees import app
from employees.database import db


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.session.execute("delete from employee")
            db.session.commit()
        yield client


def test_create(client):
    # When
    client.post("/api/employees", json={"name": "John Doe"})    
    # Then
    response = client.get("/api/employees")
    json_data = response.get_json()
    assert response.status_code == 200
    assert len(json_data) == 1
    assert json_data[0]["name"] == "John Doe"


def test_update(client):
    # Given
    response = client.post("/api/employees", json={"name": "John Doe"})
    employee_id = response.get_json()["id"]
    # When
    client.put(f"/api/employees/{employee_id}", json={"name": "Jack Doe"})

    # Then
    response = client.get(f"/api/employees/{employee_id}")
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["name"] == "Jack Doe"


def test_delete(client):
    # Given
    response = client.post("/api/employees", json={"name": "John Doe"})
    employee_id = response.get_json()["id"]
    # When
    client.delete(f"/api/employees/{employee_id}")
    # Then
    response = client.get("/api/employees")
    json_data = response.get_json()
    assert response.status_code == 200
    assert len(json_data) == 0
