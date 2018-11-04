"""
增，批量添加
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


# VALUES 的值都改为 %s 就不会报错了
sql = "INSERT INTO employee (first_name, last_name, age, sex, income) VALUES (%s, %s, %s, %s, %s)"
# 批量添加
val = [
    ('fdsa', 'dddda', 30,'M', 3300),
    ('fds', 'dddfasf', 31,'M', 3301),
    ('czx', 'ddfafd', 32,'M', 3302),
    ('fasd', 'dfads', 33,'M', 3303),
    ('xasdfxxx', 'ddfdsa', 34,'M', 3304)
]

# executemany 批量执行
mycursor.executemany(sql, val)


a = 1
mydb.commit()

print(mycursor.rowcount, "记录插入成功。")






# 关闭数据库连接
mydb.close()


