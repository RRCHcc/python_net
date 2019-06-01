"""
数据库读操作练习
select
"""
import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     passwd='123456',
                     database='stu',
                     charset='utf8')
# 创建游标
cur = db.cursor()

sql = "select * from myclass where age = 13;"
# 执行语句 cur拥有查询结果
cur.execute(sql)

one_row = cur.fetchone()  # 获取查找结果的第一个
print(one_row)
print("---------------------")
find_row = cur.fetchmany(2)  # 获取查找结果前两个，参数为取几个
print(find_row)
print("---------------------") #获取查找全部结果
find_all = cur.fetchall()
print(find_all)
cur.close()
db.close()
