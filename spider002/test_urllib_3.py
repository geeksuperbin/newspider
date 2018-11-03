# coding:utf8
'''
增加 cookie 处理 
'''

from urllib import request
from urllib import parse
from http import cookiejar

url = "http://www.baidu.com"

header = {
    'User-Agent': 'Mozilla/5.0'
}


# 使用cookiejar.CookieJar()创建CookieJar对象
cjar = cookiejar.CookieJar()
# 使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象
cookie = request.HTTPCookieProcessor(cjar)
opener = request.build_opener(cookie)
# opener 安装为全局
request.install_opener(opener)

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

  