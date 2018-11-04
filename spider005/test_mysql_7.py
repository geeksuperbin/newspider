"""
查，查询一条数据
"""


import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="root", database="pycontrol", port=8809, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = "SELECT * FROM employee WHERE AGE > '%d'" % (20)

try:
    cursor.execute(sql)
    # 获取所有记录列表
    row = cursor.fetchone()
    # 打印查询结果
    first_name, last_name, age, sex, income = row
    print("first_name=%s, last_name=%s, age=%d, sex=%s, income=%d" % \
        (first_name, last_name, age, sex, income))
    print("影响行数: %d" % cursor.rowcount)
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()