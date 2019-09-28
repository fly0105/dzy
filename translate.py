#coding=utf-8
import requests
import json

English=input("请输入数据")

headers={
"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
}

datas={
"from":"zh",
"query":English,
"to":"en",
}
#post_url="https://fanyi.baidu.com/v2transapi"
post_url="http://fanyi.baidu.com/basetrans"
res=requests.post(post_url,data=datas,headers=headers)
dict_ret=json.loads(res.content.decode())
ret=dict_ret["trans"][0]["dst"]
print(ret)

