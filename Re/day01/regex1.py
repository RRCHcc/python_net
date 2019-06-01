import re

# s = "2019年,建国70周年"
# pattern = r"\d+"
# it = re.finditer(pattern, s)
# for i in it:
#     print(i.group())

# 完全匹配
# m = re.fullmatch(r"\w+","hello-1973")# 相当于人为添加^开头 $结尾
# print(m.group())
# m = re.fullmatch(r"[0-9a-zA-Z]+", "hello1973")
# print(m.group())

# 匹配开始位置
# m = re.match(r"[A-Z]\w*", "Hello World")# 相当于开头^
# print(m.group())

# 匹配第一处
m = re.search(r"\S+", "好\n嗨 哦")
print(m.group())

