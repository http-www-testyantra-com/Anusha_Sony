import requests
import json
param={"pages":2,"count":4}
r=requests.get("http://httpbin.org/get",params=param)
print(r.status_code)
print(r.text,type(r.text))
#print(json.loads(r.text))
print(r.json())
