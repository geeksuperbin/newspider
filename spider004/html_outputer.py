import pyecharts
from pyecharts import WordCloud
import random

class HtmlOutputer():
    
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        '''
        收集数据
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


