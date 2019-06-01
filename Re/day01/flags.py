import re

s = """Hello world
你好，深圳
"""
# regex = re.compile(r"\w+")
# regex = re.compile(r"\w+", flags=re.A)  # 只能匹配ascii码字符
# l = regex.findall(s)
# print(l)

#忽略字母大小写
# regex =re.compile(r"[a-z]+",flags=re.I)
# l = regex.findall(s)
# print(l)

#匹配换行
# regex = re.compile(r".+",flags=re.S)
# l = regex.findall(s)
# print(l)
#
# regex = re.compile(r"^你好",flags=re.M)
# l = regex.findall(s)
# print(l)

#正则添加注释
pattern = r"""\w+ # 第一部分
\s+ # 第二部分
\w+ # 第三部分
"""
regex = re.compile(pattern,flags=re.X)
l = regex.findall(s)
print(l)