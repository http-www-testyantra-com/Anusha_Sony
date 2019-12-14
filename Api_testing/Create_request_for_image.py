import requests

r=requests.get(("https://xkcd.com/353/"))
print(r)
print(r.status_code)
f=open("C:\\Users\\kameswararaop\\Desktop\\My Documents\\Api_Akshay\\ApiImage.png","wb")
f.write(r.content)
print(r.content)
f.close()