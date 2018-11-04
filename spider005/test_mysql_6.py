"""
改
"""


import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="root", database="pycontrol", port=8809, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = "UPDATE employee SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')

try:
    # 执行 SQL 语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    db.rollback()
    



# 关闭数据库连接
db.close()