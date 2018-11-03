from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse

class HtmlParser():

    def __get_new_urls(self, page_url, soup):
        '''
        发现新的url
        '''
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/"))
        for link in links:
            new_url = link['href']
            new_full_url = 'http://baike.baidu.com'+ new_url
            new_urls.add(new_full_url)

        return new_urls
    

    def __get_new_data(self, page_url, soup):
        '''
        获取内容
        '''
        res_data = dict()

        res_data['url'] = page_url
        
        # 获取标题
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>***</h1> </dd>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1').get_text().strip()

        # 获取简介
        # <div class="lemma-summary">***<div>
        content_node = soup.find('div', class_='lemma-summary').get_text().strip()

        res_data['title'] = title_node
        res_data['content'] = content_node

        return res_data



    def parse(self, page_url, html_content):
        '''
        解析 html
        '''  
        if page_url is None or html_content is None:
            return
        
        soup = BeautifulSoup(html_content, 'html.parser')

        new_urls = self.__get_new_urls(page_url, soup)
        new_data = self.__get_new_data(page_url, soup)

        return new_urls, new_data