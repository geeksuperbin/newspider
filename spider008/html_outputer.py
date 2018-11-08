import pyecharts
from pyecharts import WordCloud
import random
import pymysql
import csv

class HtmlOutputer():
    
    def __init__(self):
        # self.datas = []
        # 打开数据库连接
        self.db = pymysql.connect(host="192.168.0.239", user="root", password="root123", database="cnvd", port=3306, charset='utf8')
        # self.db = pymysql.connect(host="localhost", user="root", password="root", database="cnvd", port=8809, charset='utf8')
        self.cursor = self.db.cursor()

    def collect_detail_data(self, data):
        '''
        收集详情数据
        '''
        if data is None:
            return
        self.datas.append(data)

        
    def output_html(self):
        '''
        输出数据
        '''
        if self.datas is None or len(self.datas) == 0:
            return
        
        # 写文件
        fout = open('output.html', 'w')
        
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['content'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")


        fout.close()
    
    def output_cloud(self):
        title = []
        hot = []

        if self.datas is None or len(self.datas) == 0:
            return

        for data in self.datas:
            title.append(data['title'])
            hot.append(random.randint(100,1000))

        myWordCloud = WordCloud("词云",width=1000, height=620)

        myWordCloud.add(
            "", 
            title, 
            hot,
            word_size_range=[20,100],
        )
        myWordCloud.render('./word-cloud.html')


    def output_mysql(self, data):
        '''
        输出数据到mysql
        '''
        # for data in self.datas:
        hole_info = data['hole_info']
        cnvd = data['cnvd']
        pub_time = data['pub_time']
        danger_lev = data['danger_lev']
        affect_pro = data['affect_pro']
        bugtraq = data['bugtraq']
        cve = data['cve']
        hole_desc = data['hole_desc']
        ref_url = data['ref_url']
        hole_sol_way = data['hole_sol_way']
        patch = data['patch']
        verified = data['verified']
        report_time = data['report_time']
        record_time = data['record_time']
        upd_time = data['upd_time']
        hole_file = data['hole_file']

        if hole_info is None:
            return

        sql = "INSERT INTO vul_lib_cnvd \
        (hole_info, cnvd, pub_time, danger_lev, affect_pro, bugtraq, cve, hole_desc, ref_url, hole_sol_way, patch, verified, report_time, record_time, upd_time, hole_file) VALUES \
        ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
        (hole_info, cnvd, pub_time, danger_lev, affect_pro, bugtraq, cve, hole_desc, ref_url, hole_sol_way, patch, verified, report_time, record_time, upd_time, hole_file)

        # failed_url = open('sql.csv', 'a', newline='',encoding="utf-8") 
        # write_failed = csv.writer(failed_url)
        # write_failed.writerow([sql])
        # write_failed.writerow(['------------------------'])


        # print(sql)        
        # a = 1

        # b = 2

        


        try:
            # 执行 sql 语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()

        # 关闭数据库连接
        # self.db.close()
    
    def output_csv(self):
        '''
        输出数据到csv
        '''
        pass
    
    def output_json(self):
        '''
        输出数据到json
        '''
        pass
    
    def close_database(self):
        # 关闭数据库连接
        self.db.close()