"""
使用 mysql-connector 驱动连接数据库
"""

from mysql import connector

mydb = connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="pycontrol",
    port=8809
)

# 使用 cursor() 方法创建一个游标对象 cursor
mycursor = mydb.cursor()

# 使用 execute() 方法执行 SQL 语句
mycursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据
data = mycursor.fetchone()

# 打印从数据库获取的数据
print("Database version2 : %s" % data)

# 关闭数据库连接
mydb.close()


