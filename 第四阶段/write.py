f = open('test.txt', 'r+', encoding="utf-8") # 以读写的方式打开文件
print(f.read())
f.write('\n新增内容')    # 写入新增内容
f = open('test.txt', 'r', encoding="utf-8") # 读取内容
print(f.read())
