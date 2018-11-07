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
    
    def __get_detail_content(self, content):
        '''
        获取详情内容
        beautifulsoup 没搞定，哼，祭出正则
        '''
        detail_content = {}

        # 漏洞信息
        hole_info_pattern = '<h1.*?>([\s\S]*?)<\/h1>'
        hole_info = re.findall(hole_info_pattern, content)
        if hole_info:
            hole_info = hole_info[0].strip()
        else:
            hole_info = ''
        
        # cnvd 编号
        cnvd_pattern = '<td class="alignRight">CNVD-ID</td>[\s\S]*?<td>([\s\S]*?)</td>'
        cnvd = re.findall(cnvd_pattern, content)
        if cnvd:
            cnvd = cnvd[0].strip()
        else:
            cnvd = ''

        # 公开日期
        pub_time_pattern = '<td class="alignRight">公开日期</td>[\s\S]*?<td>([\s\S]*?)</td>'
        pub_time = re.findall(pub_time_pattern, content)
        if pub_time:
            pub_time = pub_time[0].strip()
        else:
            pub_time = ''

        # 危害级别
        danger_content_pattern = '<td class="alignRight">危害级别</td>[\s\S]*?<td class="denle">([\s\S]*?)</td>'
        danger_content = re.findall(danger_content_pattern, content)
        if danger_content:
            danger_lev = self.clear_html_re(danger_content[0]).strip()
        else:
            danger_lev = ''

        # 影响产品
        affect_pro_pattern = '<td class="alignRight">影响产品</td>[\s\S]*?<td>([\s\S]*?)</td>'
        affect_pro = re.findall(affect_pro_pattern, content)
        if affect_pro:
            affect_pro = affect_pro[0].strip()
            affect_pro = self.clear_html_re(affect_pro)
        else:
            affect_pro = ''

        # bugtraq 编号
        bugtraq_pattern = '<td class="alignRight">BUGTRAQ ID</td>[\s\S]*?<td>[\s\S]*?<a[\s\S]*?>([\s\S]*?)</a>[\s\S]*?</td>'
        bugtraq = re.findall(bugtraq_pattern, content)
        if bugtraq:
            bugtraq = bugtraq[0].strip()
        else:
            bugtraq = ''


        # cve 编号
        cve_pattern = '<td class="alignRight">CVE ID</td>[\s\S]*?<td>[\s\S]*?<a[\s\S]*?>([\s\S]*?)</a>[\s\S]*?</td>'
        cve = re.findall(cve_pattern, content)
        if cve:
            cve = cve[0].strip()
        else:
            cve = ''


        # 漏洞描述
        hole_desc_pattern = '<td class="alignRight">漏洞描述</td>[\s\S]*?<td>([\s\S]*?)</td>'
        hole_desc = re.findall(hole_desc_pattern, content)
        if hole_desc:
            hole_desc = self.clear_html_re(hole_desc[0].strip())
        else:
            hole_desc = ''


        # 参考链接
        ref_url_pattern = '<td class="alignRight">参考链接</td>[\s\S]*?<td>([\s\S]*?)</td>'
        ref_url = re.findall(ref_url_pattern, content)
        if ref_url:
            ref_url = self.clear_html_re(ref_url[0]).strip()
        else:
            ref_url = ''
        
        # 漏洞解决方案
        hole_sol_way_pattern = '<td class="alignRight">漏洞解决方案</td>[\s\S]*?<td>([\s\S]*?)</td>'
        hole_sol_way = re.findall(hole_sol_way_pattern, content)
        if hole_sol_way:
            hole_sol_way = self.clear_html_re(hole_sol_way[0]).strip()
        else:
            hole_sol_way = ''

        # 厂商补丁，先采集补丁的名称，补丁详细信息单独采集
        patch_pattern = '<td class="alignRight">厂商补丁</td>[\s\S]*?<td>([\s\S]*?)</td>'
        patch = re.findall(patch_pattern, content)
        if patch:
            patch = self.clear_html_re(patch[0]).strip()
        else:
            patch = ''

        # 验证信息
        verified_pattern = '<td class="alignRight">验证信息</td>[\s\S]*?<td>([\s\S]*?)</td>'
        verified = re.findall(verified_pattern, content)
        if verified:
            verified = self.clear_html_re(verified[0]).strip()
        else:
            verified = ''

        # 报送时间
        report_time_pattern = '<td class="alignRight">报送时间</td>[\s\S]*?<td>([\s\S]*?)</td>'
        report_time = re.findall(report_time_pattern, content)
        if report_time:
            report_time = self.clear_html_re(report_time[0]).strip()
        else:
            report_time = ''

        # 收录时间
        record_time_pattern = '<td class="alignRight">收录时间</td>[\s\S]*?<td>([\s\S]*?)</td>'
        record_time = re.findall(record_time_pattern, content)
        if record_time:
            record_time = self.clear_html_re(record_time[0]).strip()
        else:
            record_time = ''

        # 更新时间
        upd_time_pattern = '<td class="alignRight">更新时间</td>[\s\S]*?<td>([\s\S]*?)</td>'
        upd_time = re.findall(upd_time_pattern, content)
        if upd_time:
            upd_time = self.clear_html_re(upd_time[0]).strip()
        else:
            upd_time = ''

        # 漏洞附件
        hole_file_pattern = '<td class="alignRight">漏洞附件</td>[\s\S]*?<td>([\s\S]*?)</td>'
        hole_file = re.findall(hole_file_pattern, content)
        if hole_file:
            hole_file = self.clear_html_re(hole_file[0]).strip()
        else:
            hole_file = ''

        return {
            'hole_info':hole_info,
            'cnvd':cnvd,
            'pub_time':pub_time,
            'danger_lev':danger_lev,
            'affect_pro':affect_pro,
            'bugtraq':bugtraq,
            'cve':cve,
            'hole_desc':hole_desc,
            'ref_url':ref_url,
            'hole_sol_way':hole_sol_way,
            'patch':patch,
            'verified':verified,
            'report_time':report_time,
            'record_time':record_time,
            'upd_time':upd_time,
            'hole_file':hole_file
        }


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
        
        detail_content = self.__get_detail_content(detail_content)

        return detail_content
    

    def clear_html_re(self, content):
        '''
        正则清除HTML标签
        :param content:原文本
        :return: 清除后的文本
        '''
        s_content = re.sub(r"</?(.+?)>|&nbsp;|\t|\r", "", content)
        s_content = re.sub(r"\n", " ", s_content)
        s_content = re.sub(r"\*", "\\*", s_content)

        return s_content

         