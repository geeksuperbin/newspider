"""
创建一张表
"""

import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="root", database="pycontrol", port=8809, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL 语句
# 创建一张数据表，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS employee")

# 使用预处理语句创建表
sql = """CREATE TABLE employee (
         first_name   CHAR(20)  NOT NULL,
         last_name    CHAR(20),
         age  INT,
         sex  CHAR(1),
         income FLOAT)"""

# 执行建表语句
cursor.execute(sql)

# 关闭数据库连接
db.close()