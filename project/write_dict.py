import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     passwd='123456',
                     database='dirct01',
                     charset='utf8')
# 创建游标
cur = db.cursor()
fd = open("dict.txt", "r")
while True:
    data = fd.readline()
    if not data:
        print("结束")
        break
    word = data[:16:].strip()
    content = data[16::].strip()
    try:
        # 插入
        sql = "insert into Dict (word,content) values \
                (%s,%s);"
        cur.execute(sql, [word, content])
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

fd.close()
cur.close()
db.close()
