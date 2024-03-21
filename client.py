import requests

response=requests.post(
    "http://localhost:8000/essay/invoke",
    json={'input':{'topic':"my best friend"}})

print(response.json()['output']['content'])