"""
    二进制存储到数据库
"""
import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     passwd='123456',
                     database='stu',
                     charset='utf8')
# 创建游标
cur = db.cursor()

# 存储文件
# with open("timg.jpeg", "rb") as fd:
#     data = fd.read()
# sql = "insert into Images values(1,'timg.jpeg',%s);"
# try:
#     # 用execute 自动传参的方法将二进制内容传人语句
#     cur.execute(sql, [data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

#获取文件
sql = "select * from Images where filename = 'timg.jpeg';"
cur.execute(sql)
image = cur.fetchone()
with open(image[1],'wb') as fd:
    fd.write(image[2])



cur.close()
db.close()
