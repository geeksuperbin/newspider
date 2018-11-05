import helper_redis
import csv


class UrlManager():
    def __init__(self):
        self.myredis = helper_redis.RedisHelper(15)
        # 存储列表url集合初始化
        self.myredis.del_redis_set('cnvd:list')
        # 初始化详情url
        self.myredis.del_redis_set('cnvd:detail:new')




    def add_list_url(self, url, offset, limit):
        '''
        添加全量列表url
        url 入口url
        offset 最大偏移量
        limit 
        '''
        
        if url is None or offset is None or limit is None:
            return

        
        
        # 存储列表url
        # http://www.cnvd.org.cn/flaw/list.htm?max=100&offset=0
        count = 0
        while count <= limit:
            url = "http://www.cnvd.org.cn/flaw/list.htm?max=%d&offset=%d" % (offset, count)
            count += offset
            self.myredis.add_redis_data('cnvd:list', url)

    
    
    def get_list_url(self):
        '''
        获得一个待爬取列表url
        '''
        new_url = self.myredis.get_one_data('cnvd:list')
        return new_url 


    def add_detail_urls(self, detail_urls):
        '''
        批量添加详情 urls
        '''

       

        # csv 文件备份
        csv_file = open('detail_new_urls.csv', 'a', newline='')
        csv_write = csv.writer(csv_file)

        for detail_url in detail_urls:
            if self.myredis.exist_detail_url('cnvd:detail:new',detail_url) or self.myredis.exist_detail_url('cnvd:detail:old',detail_url):
               continue
            self.myredis.add_redis_data('cnvd:detail:new',detail_url)
            csv_write.writerow([detail_url])


    def has_list_url(self):
        '''
        是否有待爬取的列表url
        '''
        num = self.myredis.get_num('cnvd:list')
        return num
            
        



    def has_detail_url(self):
        '''
        是否有待爬取的详情url
        '''
        pass

    
    def get_detail_url(self):
        '''
        获取一个待爬取详情url
        '''
        pass

   