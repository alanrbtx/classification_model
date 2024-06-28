import requests


res = requests.get("http://127.0.0.1:8000/get_test_prediction")
print(res)
res.json().get("result")
print("--------------------------------")
print("TEST ENDPOINT RESULT: ",  res.json().get("result"))

url = 'http://127.0.0.1:8000/get_real_prediction'
files = {'media': open('data/PetImages/Cat/3004.jpg', 'rb')}
res = requests.post(url, files=files)
res.json().get("result")
print("--------------------------------")
print("ENDPOINT RESULT: ",  res.json().get("result"))
print("--------------------------------")