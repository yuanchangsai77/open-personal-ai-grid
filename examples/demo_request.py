import requests

r = requests.post(
    "http://127.0.0.1:8000/task",
    json={"text": "记一笔米线14"}
)

print(r.json())