
'''
爬虫调度程序
'''

import url_manager, html_downloader, html_parser, html_outputer



class SpiderMain():
    def __init__(self):

        '''
        构造函数初始化注册，包括
        URL 管理器
        网页下载器
        网页解析器    
        '''

        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        # 统计爬取的是第几个url
        count = 1
        '''
        爬虫调度,实现时序图功能。ps:时序图真好用
        '''
        
        # 添加待爬url
        self.urls.add_new_url(root_url)
        
        # 有待爬取的url？
        while self.urls.has_new_url():
            # 异常处理，代码保护
            try:
                # 是的则获取一个待爬url
                new_url = self.urls.get_new_url()
                # 监控爬取的是第几个url
                print('craw %d : %s' % (count, new_url))
                # 下载 url 内容
                html_content = self.downloader.download(new_url)
                # 解析 url 内容,维护两个set集合，一个是已爬取url，一个是未爬取url，同时利用集合不重复元素特性 
                new_urls, new_data = self.parser.parse(new_url, html_content)

                a = 1
                # 批量添加 url
                self.urls.add_new_urls(new_urls)
                # 收集数据
                self.outputer.collect_data(new_data)
            except:
               print('craw failed: %s' % (new_url))

            # 内容统计到1000条时输出内容
            if count >= 200:
                break

            # 计数器加一
            count +=1

        # 输出数据
        self.outputer.output_html()
        # 内容云
        self.outputer.output_cloud()


if __name__=='__main__':
    # 爬虫入口url
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
