"""
增，占位符形式
"""


import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="root", database="pycontrol", port=8809, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

first_name = 'fff'
last_name = 'ggg'
age = 33
sex = 'F'
income = 3000

# 构建 SQL 语句
sql = "INSERT INTO employee \
(first_name, last_name, age, sex, income) VALUES \
('%s', '%s', '%d', '%c', '%d')" % \
(first_name, last_name, age, sex, income)

try:
    # 执行 sql 语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    print('111')
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()