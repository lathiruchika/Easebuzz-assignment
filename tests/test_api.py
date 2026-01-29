import requests
import time
import json
from jsonschema import validate
import pytest

def test_posts_response(base_url):
    response = requests.get(f"{base_url}/posts")
    assert response.status_code == 200

def test_response_time(base_url):
    start = time.time()
    response = requests.get(f"{base_url}/posts")
    assert time.time() - start < 2

def test_schema_validation(base_url):
    response = requests.get(f"{base_url}/posts/1")
    with open("schemas/post_schema.json") as f:
        schema = json.load(f)
    validate(instance=response.json(), schema=schema)

@pytest.mark.parametrize("endpoint", ["/posts", "/comments", "/users"])
def test_multiple_endpoints(base_url, endpoint):
    response = requests.get(f"{base_url}{endpoint}")
    assert response.status_code == 200