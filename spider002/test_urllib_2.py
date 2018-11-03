# coding:utf8
'''
    增加头信息
'''
from urllib import request
from urllib import parse

url = "http://www.baidu.com"

header = {
    'User-Agent': 'Mozilla/5.0'
}

# 构造头信息
req = request.Request(url, headers=header)
# 发送请求
reponse = request.urlopen(req)
# 读取请求
htmls = reponse.read()
# 响应状态
code = reponse.getcode()
# 内容转码
htmls = str(htmls, encoding="utf-8")

a=1

  