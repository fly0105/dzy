import requests

url=input("请输入url：")
res=requests.get(url)

with open ("a.png","wb") as f:
    f.write(res.content)
