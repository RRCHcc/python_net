"""
练习：
    创建一个数据表为user
    编写程序完成如下功能
        *注册，终端输入用户名和密码，将用户名密码
         存入打数据库中，用户名不能重复
        *登录，从终端输入用户名和密码，如果该用户
         名存在则得到登录成功，不存在则得到登录失败
    将数据库操作功能封装为类
"""
import pymysql

class Login:
    def __init__(self,
                 database='user',
                 host='localhost',
                 user='root',
                 passwd='123456',
                 port=3306,
                 charset='utf8',
                 table='login'):
        self.database = database
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.charset = charset
        self.table = table
        self.connect_db()  # 连接数据库

    def connect_db(self):
        self.db = pymysql.connect(host=self.host,
                                  user=self.user,
                                  port=self.port,
                                  database=self.database,
                                  passwd=self.passwd,
                                  charset=self.charset)
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def login(self, name, passwd):
        sql = "select * from %s where name ='%s' and passwd='%s';" \
              % (self.table, name, passwd)
        self.cur.execute(sql)
        if self.cur.fetchone():
            return True
        else:
            return False

    def register(self, name, passwd):
        sql = "select * from %s where name ='%s';" % (self.table, name)
        self.cur.execute(sql)
        if self.cur.fetchone():
            return False

        sql = "insert into %s (name,passwd) values('%s','%s');" % \
              (self.table, name, passwd)
        try:
            self.cur.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
            return False
        return True
