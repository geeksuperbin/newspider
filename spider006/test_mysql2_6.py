"""
查，查询一条数据
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


sql = "SELECT * FROM employee WHERE age > %s"
val = (1,)

mycursor.execute(sql, val)

# 没有以下这句话
# mydb.commit()

row = mycursor.fetchone()

first_name, last_name, age, sex, income = row
print("first_name=%s, last_name=%s, age=%d, sex=%s, income=%d" % \
    (first_name, last_name, age, sex, income))

print("影响行数: %d" % mycursor.rowcount)

# 关闭数据库连接
mydb.close()


