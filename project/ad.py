fd = open("dict.txt","r")
while True:
    data = fd.readline()
    if not data:
        break
    info = data[:17]
    content = data[17:]
    print(info.strip())
