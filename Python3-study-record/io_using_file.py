poem = '''\
# Programming is fun
# When the work is done
# if you wanna make your work also fun:
#    use Python!
'''

# 打开文件以编辑（'w'riting）
f = open('./test/1.py', 'w')
# 向文件中编写文本
f.write(poem)
# 关闭文件
f.close()
''' 三引号干了啥？
其实就是多行注释
'''
# 如果没有特别指定，
# 将假定启用默认的阅读（'r'ead）模式
f = open('./test/1.py')
while True:
    line = f.readline()
    # 零长度指示 EOF
    if len(line) == 0:
        break
    # 每行（`line`）的末尾
    # 都已经有了换行符
    #因为它是从一个文件中进行读取的
    print(line, end='')
# 关闭文件
f.close()