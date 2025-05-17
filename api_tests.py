import requests
import logging

# Logger sozlash
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    logging.info("GET /posts")
    assert response.status_code == 200, "Status code 200 emas"
    assert isinstance(response.json(), list), "Response list emas"
    logging.info("✅ GET testi o'tdi")

def test_post_new_post():
    data = {
        "title": "Test title",
        "body": "This is a test body",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=data)
    logging.info("POST /posts")
    assert response.status_code == 201, "Status code 201 emas"
    json_data = response.json()
    assert json_data["title"] == data["title"], "Title mos emas"
    assert json_data["body"] == data["body"], "Body mos emas"
    logging.info("✅ POST testi o'tdi")

def test_put_post():
    data = {
        "id": 1,
        "title": "Updated title",
        "body": "Updated body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=data)
    logging.info("PUT /posts/1")
    assert response.status_code == 200, "Status code 200 emas"
    json_data = response.json()
    assert json_data["title"] == data["title"], "Title yangilanmadi"
    logging.info("✅ PUT testi o'tdi")

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    logging.info("DELETE /posts/1")
    assert response.status_code == 200, "Status code 200 emas"
    logging.info("✅ DELETE testi o'tdi")

if __name__ == "__main__":
    test_get_posts()
    test_post_new_post()
    test_put_post()
    test_delete_post()
    logging.info("Barcha testlar muvaffaqiyatli yakunlandi.")