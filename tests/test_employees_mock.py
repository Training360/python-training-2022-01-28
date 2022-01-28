import pytest
from employees import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_find_all(client, mocker):
    mocker.patch(
        'employees.models.find_all',
        return_value=[{"name": "Jack Doe"}, {"name": "Jane Doe"}]
    )

    response = client.get("/api/employees")
    json_data = response.get_json()
    assert response.status_code == 200
    assert len(json_data) == 2
