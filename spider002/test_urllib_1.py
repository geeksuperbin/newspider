# coding:utf8
from urllib import request

url = "http://www.baidu.com"

# 请求页面
response = request.urlopen(url)
# 获取响应状态码
code = response.getcode()
# 读取页面
htmls = response.read()
# 页面转码
htmls = str(htmls, encoding='utf-8')
# 内容统计
lens = len(htmls)
a = 1