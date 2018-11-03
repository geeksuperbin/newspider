

class UrlManager():
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()



    def add_new_url(self, url):
        '''
        添加新的url
        '''
        
        if url is None:
            return
        
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
        




    def add_new_urls(self, urls):
        '''
        批量添加 urls
        '''

        if urls is None or len(urls) == 0:
            return
        
        for url in urls:
            self.add_new_url(url)
        




    def has_new_url(self):
        '''
        是否有需要爬取的url
        '''

        # True 为有爬取的url
        # False 没有爬取的url
        return len(self.new_urls)
        
        

    def get_new_url(self):
        '''
        获得一个待爬取的url
        '''

        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)

        return new_url 


   