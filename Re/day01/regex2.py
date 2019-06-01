import re

pattern = r"(ab)cd(?P<pig>ef)"

regex = re.compile(pattern)

# 获取match对象
obj = regex.search("abcdefghi", pos=0, endpos=7)

# 属性变量
print(obj.pos)  # 目标字符串开始位置
print(obj.endpos)  # 目标字符串结束位置
print(obj.re)  # 正则表达式
print(obj.string)  # 目标字符串
print(obj.lastgroup)  # 最后一组名称
print(obj.lastindex)  # 最后一组序号
print("---------------------")

# 属性方法
print(obj.start())  # 开始
print(obj.end())  # 结束
print(obj.span())  # 开始和结束
print(obj.groupdict())  # 捕获组字典
print(obj.groups())  # 子组对应内容
print(obj.group(1))     # 组序号
print(obj.group("pig"))     #组名
