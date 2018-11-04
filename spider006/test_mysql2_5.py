"""
改
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


sql = "UPDATE employee SET first_name = %s WHERE last_name = %s "
val = ('Geekbin', 'ggg')

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, " 条记录被修改")





# 关闭数据库连接
mydb.close()


