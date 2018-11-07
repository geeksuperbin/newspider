import helper_redis
import csv
import pymysql


class UrlManager():
    def __init__(self):
        # self.myredis = helper_redis.RedisHelper(15)
        # 存储列表url集合初始化
        # self.myredis.del_redis_set('cnvd:list')
        # 初始化详情url
        # self.myredis.del_redis_set('cnvd:detail:new')
        self.datail_data_urls = set()
        self.add_history_detail()
        # print(len(self.datail_data_urls))
        # exit()




    def add_list_url(self, url, offset, limit):
        '''
        添加全量列表url
        url 入口url
        offset 最大偏移量
        limit 
        '''
        
        if url is None or offset is None or limit is None:
            return

        # url = "http://www.cnvd.org.cn/flaw/list.htm?max=100&offset=10700"
        # self.myredis.add_redis_data('cnvd:list', url)
        
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
            if detail_url not in self.datail_data_urls:
                self.datail_data_urls.add(detail_url)
                csv_write.writerow([detail_url])
            # if self.myredis.exist_detail_url('cnvd:detail:new',detail_url) or self.myredis.exist_detail_url('cnvd:detail:old',detail_url):
            #    continue
            # self.myredis.add_redis_data('cnvd:detail:new',detail_url)
                


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
        return len(self.datail_data_urls)

    
    def get_detail_url(self):
        '''
        获取一个待爬取详情url
        '''
        detail_url = self.datail_data_urls.pop()
        return detail_url


    def add_history_detail(self):
        '''
        从文件中读取详情url到集合中
        '''
        # db = pymysql.connect(host="localhost", user="root", password="root", database="cnvd", port=8809, charset='utf8')
        db = pymysql.connect(host="192.168.0.239", user="root", password="root123", database="cnvd", port=3306, charset='utf8')
        cursor = db.cursor()
        # 从数据库中读取已处理的url，并进行剔除操作
        data_filter = set()
        sql = "SELECT cnvd FROM vul_lib_cnvd"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            r  = 'http://www.cnvd.org.cn/flaw/show/'+row[0]
            data_filter.add(r)

        csv_file = csv.reader(open('detail_new_urls.csv', 'r'))

        for detail_url in csv_file:
            if detail_url[0] not in data_filter:
                self.datail_data_urls.add (detail_url[0])
                # failed_url = open('download_failed_detail_urls.csv', 'a', newline='') 
                # write_failed = csv.writer(failed_url)
                # write_failed.writerow([detail_url[0]])