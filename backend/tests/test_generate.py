from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_generate_valid_code():
    response = client.post(
        "/generate",
        json={
            "prompt": "Write a Python function to reverse a string",
            "language": "Python"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert "code" in data
    assert data["code"] != ""



def test_ambiguous_prompt():
    response = client.post(
        "/generate",
        json={
            "prompt": "write me a code",
            "language": "Python"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert data["code"] == ""
    assert "ambiguous" in data["explanation"].lower()



def test_empty_prompt():
    response = client.post(
        "/generate",
        json={
            "prompt": "",
            "language": "Python"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert data["code"] == ""



def test_invalid_language():
    response = client.post(
        "/generate",
        json={
            "prompt": "Write a program to add two numbers",
            "language": "C++"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert "code" in data
    assert data["code"] == ""
    assert "explanation" in data

