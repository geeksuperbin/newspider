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
    
    def __get_detail_content(self, soup):
        '''
        获取详情内容
        '''
        detail_content = {}
        # 漏洞信息
        holeInfo  = soup.find('h1').get_text()
        # cnvd 编号
        # cnvd = soup.find_all('tr')[0].find_all('td')[1].get_text().strip()
        cnvd = soup.find('td', text='CNVD-ID')
        # cnvd = soup.find_all('tr')[0]
        # 公开日期
        # pubTime = soup.find_all('tr')[0]
        # 危害级别
        # 影响产品
        # bugtraq 编号
        # cve 编号
        # 漏洞描述
        # 参考链接
        # 漏洞解决方案
        # 厂商补丁，先采集补丁的名称，补丁详细信息单独采集
        # 验证信息
        # 报送时间
        # 收录时间
        # 更新时间
        # 漏洞附件


        print(cnvd)
    



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
        if detail_content is None:
            return
        
        soup = BeautifulSoup(detail_content, 'html.parser')

        detail_content = self.__get_detail_content(soup)

        return detail_content