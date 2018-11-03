import pyecharts
from pyecharts import WordCloud

"""
词云图主要用 热词的热度 进行可视化。
WordCloud.add() 方法签名 
add(name, attr, value, 
shape=”circle”, 
word_gap=20, 
word_size_range=None, 
rotate_step=45) 
name -> str：图例名称 
attr -> list：属性名称 
value -> list：属性所对应的值 
shape -> list：词云图轮廓，有 circle, cardioid, diamond, 
triangleforward, triangle, pentagon, star 可选 
word_gap -> int：单词间隔，默认为 20。 
word_size_range -> list：单词字体大小范围，默认为 [12, 60]。 
rotate_step -> int：旋转单词角度，默认为 45
"""


myWordCloud = WordCloud("",width=1000, height=620)
name = ['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 
        'Charter Communications', 'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 
        'Express', 'Home', 'Johnny Depp', 'Lena Dunham',
        'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham', 
        'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break'] 
value = [ 100, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965,
         847, 582, 555, 550, 462, 366, 360, 282, 273, 265] 
# value = [ 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
#          100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

myWordCloud.add(
    "", 
    name, 
    value,
    word_size_range=[20,100],
)
myWordCloud.render('./word-cloud.html')