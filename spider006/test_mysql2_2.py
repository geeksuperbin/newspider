"""
增
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

first_name = 'fff'
last_name = 'ggg'
age = 33
sex = 'F'
income = 3000

# VALUES 的值都改为 %s 就不会报错了
sql = "INSERT INTO employee (first_name, last_name, age, sex, income) VALUES (%s, %s, %s, %s, %s)"
val = (first_name, last_name, age, sex, income)


# 组合查询结构和查询数据
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "记录插入成功。")






# 关闭数据库连接
mydb.close()


