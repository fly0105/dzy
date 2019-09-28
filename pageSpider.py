#coding=utf-8
import requests
import re

class Page:
    def __init__(self,url):
        self.url=url;
        self.headers={
                       "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0" ,
                }
    
    def send_request(self,url):
        res=requests.get(url,headers=self.headers)
        return res.content.decode()

    def get_content(self,res_content):
        content=re.findall(r"<p>(.*?)</p>",res_content,re.S)
        print(content)

    def run(self):
        res_content=self.send_request(self.url)
        self.get_content(res_content);

if __name__=="__main__":
    url=input("请输入url：")
    page=Page(url);
    page.run()

