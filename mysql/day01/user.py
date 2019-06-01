from login import Login

user = Login()


# 成功返回TURE 失败FALSE
def do_login():
    name = input("User>>>")
    passwd = input("passwd>>>")
    return user.login(name, passwd)


def do_register():
    name = input("User>>>")
    passwd = input("passwd>>>")
    return user.register(name, passwd)


while True:
    print("-------------------")
    print("***    login    ***")
    print("***   register  ***")
    print("-------------------")

    cmd = input("Cmd:")
    if cmd == 'login':
        if do_login():
            print("登录成功")
        else:
            print("登录失败")
        break
    elif cmd == 'register':
        if do_register():
            print("注册成功")
        else:
            print("注册失败")
        break
    else:
        print("输入错误,重新输入")

user.close()
