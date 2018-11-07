from urllib import request
from urllib import parse
from http import cookiejar
# import socket

class HtmlDownloader():
    
    def download_list_content(self, url):
        '''
        下载列表url内容
        '''
        if url is None:
            return
        
        header = {
            'User-Agent': 'Mozilla/5.0'
        }
        # socket.setdefaulttimeout(60)
        cjar = cookiejar.CookieJar()
        cookie = request.HTTPCookieProcessor(cjar)
        opener = request.build_opener(cookie)
        request.install_opener(opener)

        req = request.Request(url, headers=header)
        reponse = request.urlopen(req)
        htmls = reponse.read()
        code = reponse.getcode()

        if code != 200:
            return
        
        htmls = str(htmls, encoding="utf-8")

        return htmls

    
    def download_detail_content(self, url):
        '''
        下载详情url内容
        '''
        if url is None:
            return
        try:
            header = {
                'User-Agent': 'Mozilla/5.0'
            }
            cjar = cookiejar.CookieJar()
            cookie = request.HTTPCookieProcessor(cjar)
            opener = request.build_opener(cookie)
            request.install_opener(opener)

            req = request.Request(url, headers=header)
            reponse = request.urlopen(req)
            htmls = reponse.read()
            code = reponse.getcode()

            if code != 200:
                raise RuntimeError('htmlError')
            
            htmls = str(htmls, encoding="utf-8")

            return htmls
        except:
            failed_url = open('F:\\develop\\code\\python3\\newspider\\spider008\\html_failed_detail_urls.csv', 'a', newline='') 
            # failed_url = open('html_failed_detail_urls.csv', 'a', newline='') 
            write_failed = csv.writer(failed_url)
            write_failed.writerow([url])        
