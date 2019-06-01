"""
缓冲
"""

# fd = open("text", "w", 0)#无缓冲(不允许
# fd = open("text", "w", 1)#行缓冲
fd = open("text", "w", 12)#指明缓冲大小
while True:
    s = input(">>")
    fd.write(s+'\n')
    fd.flush()  #立即刷新缓冲区，将内容写入磁盘

    fd.close()


