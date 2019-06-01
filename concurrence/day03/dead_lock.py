"""

        死锁及其处理

"""
import time
import threading


# 交易类
class Account:
    def __init__(self, id, balance, lock):
        self.id = id  # 用户
        self.balance = balance  # 存款
        self.lock = lock  # 锁

    # 获取金钱
    def get_money(self):
        return self.balance

    # 取钱
    def withdraw(self, amount):
        self.balance -= amount

    # 存钱
    def deposit(self, amount):
        self.balance += amount


# 转账函数
def transfer(from_, to, amount):
    if amount > from_.balance:
        print("超过账户金额")
    # 上锁成功返回True
    elif from_.lock.acquire():  # 锁住自己的账户
        from_.withdraw(amount)  # 自己账户金额减少
        time.sleep(0.1)
        if to.lock.acquire():
            to.deposit(amount)  # 对方账户金额增加
            to.lock.release()  # 对方账户解锁
        from_.lock.release()  # 自己账户解锁
        print("转账完成")


# 创建两个账户
QTX = Account("QTX", 5000, threading.Lock())
kop = Account("KOP", 3000, threading.Lock())

t = threading.Thread(target=transfer, args=(QTX, kop, 1500))
t1 = threading.Thread(target=transfer, args=(kop, QTX, 1000))

t.start()
time.sleep(2)
t1.start()

t.join()
t1.join()
print(QTX.get_money())
print(kop.get_money())
