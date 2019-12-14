import requests
import json

param={"username":"abc","password":"123"}
r=requests.post("http://httpbin.org/post", data=param)
print(r.status_code)
print(r.text)