import re

# s = "RR:1994,Sunny:1993"
# pattern = r"(\w+):(\d+)"

# re 模块调用
# l = re.findall(pattern, s)
# print(l)
# compile 对象调用
# regex = re.compile(pattern)
# l = regex.findall(s)
# print(l)

# s = "hello world how are you L-boby"
# l = re.split(r'[^\w]+', s)  # ^写在[]里面是取反，写在外变表示开头
# l = re.split(r'\W+', s)  # ^写在[]里面是取反，写在外变表示开头
# print(l)
s = "时间：2019/10/12"
# ns = re.sub(r'/', '-', s, 1)
ns = re.sub(r'\d+', '00', s, )
print(ns)
