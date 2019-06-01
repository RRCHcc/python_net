import re
import sys

port = sys.argv[1]
f = open("1.txt")

# 找到port 段落
while True:
    data = ''
    for line in f:
        if line != '\n':  # 不是空行
            data += line
        else:
            break
    # print(">>>>", data)
    if not data:    #文件结尾
        print("Not Found the %s"%port)
        break
    # 匹配字符串首单词
    key_word = re.match(r"\S+", data).group()
    if port == key_word:
        #匹配目标内容
        # pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
        pattern = r"(\d{1,3}\.){3}\d{1,3}/\d+|Unknow"
        try:
            address = re.search(pattern,data).group()
            print(address)
        except:
            print("Not address")
            break