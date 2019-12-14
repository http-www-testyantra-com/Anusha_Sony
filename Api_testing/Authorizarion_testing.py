import requests
import json

param={"username":"abcd","password":"testing"}
r=requests.get("http://httpbin.org/basic-auth/abcd/124",auth=("abcd","124"))
print(r.status_code)
print(r.text)
