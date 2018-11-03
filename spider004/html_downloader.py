

from urllib import request
import ssl

class HtmlDownloader():
    
    def download(self, url):
        '''
        下载html内容
        '''
          
        if url is None:
            return
        
        # 请求页面
        context = ssl._create_unverified_context()
        response = request.urlopen(url, context=context)
        # 获取响应状态码
        code = response.getcode()
        # 状态码判断
        if code != 200:
            return

        # 读取页面
        htmls = response.read()
        # 页面转码
        htmls = str(htmls, encoding='utf-8')

        return htmls

        
