"""
删
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

age = 31

sql = "DELETE FROM employee WHERE age = %s"
# 一个数据项时「,」逗号不能省略，否则报错
val = (age,)

mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, " 条记录被删除")





# 关闭数据库连接
mydb.close()


