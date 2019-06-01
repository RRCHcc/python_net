"""
                        sql语句传参练习
"""
import pymysql

# 创建数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     passwd='123456',
                     database='stu',
                     charset='utf8')

# 创建游标
cur = db.cursor()
while True:
    name = input("Name：")
    age = input("Age：")
    gender = input("Gender('m' or 'w'：")
    score = input("Score:")
    # 写法一
    # sql = "insert into myclass (name,age,gender,score) value \
    # ('%s',%d,'%s',%f);" % (name, age, gender, score)
    # 写法二
    sql = "insert into myclass (name,age,gender,score) value \
        (%s,%s,%s,%s);"  # 不需要人为添加引号
    try:
        cur.execute(sql, [name, age, gender, score])  # 会自动识别数据类型
        db.commit()
    except Exception as e:
        db.rollback()  # 如果失败回滚到操作之前的状态
        print("Faild:", e)
    else:
        print("插入成功")

cur.close()
db.close()
