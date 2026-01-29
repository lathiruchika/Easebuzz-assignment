import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_posts():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

    posts = response.json()
    print(posts)
    
    required_keys = {"userId", "id", "title", "body"}

    for post in posts:
        assert required_keys.issubset(post.keys())

    with open("first_5_posts.json", "w") as f:
        json.dump(posts[:5], f, indent=4)

if __name__ == "__main__":
    fetch_posts()