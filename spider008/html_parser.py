from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse

class HtmlParser():

    def __get_detail_urls(self, soup):
        '''
        发现详情url
        '''
        detail_urls = set()
        links = soup.find_all('a', href=re.compile(r"/flaw/show/"))
        for link in links:
            new_url = link['href']
            new_full_url = 'http://www.cnvd.org.cn'+ new_url
            detail_urls.add(new_full_url)

        return detail_urls
    



    def parse_list_content(self, list_content):
        '''
        解析列表url内容
        '''  
        if list_content is None:
            return
        
        soup = BeautifulSoup(list_content, 'html.parser')

        detail_urls = self.__get_detail_urls(soup)

        return detail_urls

    
    def parse_detail_content(self, detail_content):
        '''
        解析详情url内容
        '''
        pass