"""
with 语句
"""

with open("text")as fd:#生成文件对象
    data = fd.read()
    print(data)

    #语句块结束，with 生成的对象会自动释放