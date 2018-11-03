# coding:utf8
from urllib import request
import ssl


# url = "http://www.baidu.com"
url = "http://baike.baidu.com/view/21087.htm"

# 请求页面
context = ssl._create_unverified_context()
response = request.urlopen(url, context=context)
# 获取响应状态码
code = response.getcode()
# 读取页面
htmls = response.read()
# 页面转码
htmls = str(htmls, encoding='utf-8')
# 内容统计
lens = len(htmls)
a = 1