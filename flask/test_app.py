import pytest
from app import app  # Import the Flask app

@pytest.fixture
def client():
    """
    A pytest fixture to set up the Flask test client.
    """
    with app.test_client() as client:
        yield client

def test_hello(client):
    """
    Test the '/' route for a successful response.
    """
    response = client.get("/")  # Simulate a GET request to the '/' route
    assert response.status_code == 200  # Verify the response status code
    assert response.data == b"Flask inside Docker!!"  # Verify the response body
