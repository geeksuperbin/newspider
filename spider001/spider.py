'''
模块注释
'''
from urllib import request
import ssl
import re

class Spider():
    '''
    类注释
    '''
    url = 'https://www.panda.tv/cate/pubg'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '<span class="video-nickname" title="([\s\S]*?)">'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    def __fetch_content(self):
        '''
        获取数据
        '''
        context = ssl._create_unverified_context()
        r = request.urlopen(Spider.url,context=context)
        # 这块加了一个ssl 认证，取消了字节码转换
        htmls = r.read()
        # 必须要进行转码，否则报错
        htmls = str(htmls, encoding='utf-8')

        return htmls
    
    def __analysis(self, htmls):
        '''
        提取数据
        '''
        root_html = re.findall(Spider.root_pattern, htmls)
        
        # 定义存放数据列表
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            anchor = {'name':name, 'number':number}
            anchors.append(anchor)

        return anchors

       
    def __refine(self, anchors):
        '''
        精炼数据 
        '''
        l = lambda anchor: {
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0]
        }

        return map(l, anchors)
    
    
    def __sort(self, anchors):
        '''
        分析数据
        '''
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)

        return anchors
    
    
    def __sort_seed(self, anchor):
        '''
        比较种子
        '''
        r = re.findall('[\d.]*',anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000

        return number

    
    def __show(self, anchors):
        '''
        渲染数据
        '''
        # for anchor in anchors:
        for rank in range(0, len(anchors)):
            # print(anchor['name'] + '---' + anchor['number'])
            print('rank ' + str(rank + 1)
            + ' : ' + anchors[rank]['name']
            + ' ' + anchors[rank]['number'] + ' 人')

    
    def go(self):
        '''
        开始爬虫
        '''
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


spider = Spider()
spider.go()