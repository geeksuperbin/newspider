"""
爬虫调度
"""

import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain():
    def __init__(self):

        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url, offset,limit):
        
        # 添加全量列表 url 
        self.urls.add_list_url(root_url, offset,limit)
        # exit()

        # 列表 url 处理
        list_count = 1
        while self.urls.has_list_url():
            try:
                list_url = self.urls.get_list_url()
                print('list craw %d : %s' % (list_count, list_url))
                list_content = self.downloader.download_list_content(list_url)
                detail_urls = self.parser.parse_list_content(list_content)
                self.urls.add_detail_urls(detail_urls)
            except:
               print('list craw failed: %s' % (list_url))
            list_count +=1

        print('列表 url 处理完成')

        # 详情 url 处理
        # detail_count = 1
        # while self.urls.has_detail_url():
        #     try:
        #         detail_url = self.urls.get_detail_url()
        #         print('detail craw %d : %s' % (detail_count, detail_url))
        #         detail_content = self.downloader.download_detail_content(detail_url)
        #         detail_data = self.parser.parse_detail_content(detail_content)
        #         self.outputer.collect_detail_data(detail_data)
        #     except:
        #         print('detail craw failed: %s' % (detail_url))
        #     detail_count +=1

        # # 输出数据
        # self.outputer.output_mysql()
        # self.outputer.output_csv()
        # self.outputer.output_json()


if __name__=='__main__':
    root_url = "http://www.cnvd.org.cn/flaw/list.htm?max=100&offset=0"
    obj_spider = SpiderMain()
    # obj_spider.craw(root_url)
    obj_spider.craw(root_url ,100, 114500)
