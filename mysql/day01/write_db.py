"""
    写数据库连接
"""
import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     passwd='123456',
                     database='stu',
                     charset='utf8')
# 创建游标
cur = db.cursor()

try:
    # 插入
    sql = "insert into interest values \
            (3,'Bob','draw,sing','A','8888','凑合吧');"
    cur.execute(sql)
    # 修改
    sql = "update interest set price=6666 where name='Abby';"
    cur.execute(sql)
    # 删除
    sql = "delete from myclass where score < 88;"
    cur.execute(sql)

    db.commit()
except Exception as e:
    print(e)
    db.rollback()

cur.close()
db.close()

