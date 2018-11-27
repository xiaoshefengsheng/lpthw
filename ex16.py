from sys import argv

script, filename = argv

print(f"we're going to erase {filename}.")
print("if you don't want that, hit ctrl-c (^c).")
print("if you do wangt that,hit return.")
#此处的input使得脚本保持待输入状态，可根据上面提示，如停止请ctrl+c，继续的话任意键继续即可
input("?")

print("opening the file...")
#将文件名赋值给target变量，创建该文件，即“w”参数。
target = open(filename, 'w')
#.truncate是截断文件操作，默认创建文件后，就截断的话，文件为空文件。
print("truncating the file . goodbye!")
target.truncate()

print("now i'm going to ask you for three lines.")
#接收用户输入值
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("i'm going to write these to the file.")
#将上方暂存的变量值写入到文件
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally, we close it.")
#关闭文件，避免时间过长或程序缓存的文件过多
target.close()
