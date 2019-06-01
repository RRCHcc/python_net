"""

"""
import pymysql
import hashlib
import time


class Database:
    def __init__(self,
                 host='localhost',
                 port=3306,
                 user='root',
                 passwd='123456',
                 database='dirct01',
                 charset='utf8'):

        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.charset = charset
        self.connect_db()  # 连接数据库
        self.cur = None

    def connect_db(self):
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  passwd=self.passwd,
                                  database=self.database,
                                  charset=self.charset)

    def create_cursor(self):
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    # 处理注册
    def register(self, name, passwd):
        sql = "select * from user where name = '%s'" % name
        self.cur.execute(sql)

        r = self.cur.fetchone()  # 查询到结果
        if r:
            return False

        # 加密处理
        hash = hashlib.md5((name + "wahaha").encode())
        hash.update(passwd.encode())
        sql = "insert into user (name,passwd) values (%s,%s)"

        try:
            self.cur.execute(sql, [name, hash.hexdigest()])
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            self.db.rollback()
            return False

    # 处理登录
    def login(self, name, passwd):
        hash = hashlib.md5((name + "wahaha").encode())
        hash.update(passwd.encode())
        sql = "select * from user where name =%s and passwd = %s"
        self.cur.execute(sql, [name, hash.hexdigest()])
        r = self.cur.fetchone()
        if r:
            return True
        else:
            return False

    # 插入历史记录
    def insert_history(self, name, word):
        tm = time.ctime()
        sql = "insert into history (name,content,time) values (%s,%s,%s)"
        try:
            self.cur.execute(sql, [name, word, tm])
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    # 查询单词
    def query(self, word):
        sql = "select content from Dict where word='%s'" % word
        # print("#########",sql) 测试
        self.cur.execute(sql)

        r = self.cur.fetchone()
        if r:
            return r[0]

    # 历史记录
    def history(self, name):
        sql = "select name,content,time from history where name = '%s' \
              order by id desc limit 10" % name
        self.cur.execute(sql)

        return self.cur.fetchall()

# a = Database()
# a.create_cursor()
# s = a.register('xiao','123456')
# print(s)
