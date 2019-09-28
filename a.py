#coding=utf-8
import requests
import json

post_url="https://fanyi.baidu.com/langdetect"
post_data={
        "query":"昨天",
        
}
header={
"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"        
}
res=requests.post(post_url,headers=header,data=post_data)
dict=json.loads(res.content.decode());
print(dict)
