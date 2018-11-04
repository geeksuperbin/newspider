"""
拿下 cnvd
"""
from selenium import webdriver

# http://www.cnvd.org.cn/flaw/list.htm?max=100&offset=114400
# http://www.cnvd.org.cn/flaw/show/CNVD-2018-19952
url = "http://www.cnvd.org.cn/flaw/list.htm?max=100&offset=0"
# 114467


def COOKIES(url):
    driver = webdriver.Chrome()
    driver.get(url)
    cj = driver.get_cookies()
    cookie = ''
    for c in cj:
        cookie += c['name'] +'='   + c['value'] + ';'
    return cookie
    driver.quit()

cookie = COOKIES(url)

print(cookie)