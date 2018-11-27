from sys import argv
from os.path import exists
#赋值argv变量为三个参数，脚本名和两个文件参数
script, from_file, to_file = argv
#用f输出参数变量值
print(f"copying from {from_file} to {to_file}")

#we could do these two on one line, how?
in_file = open(from_file)
#打印in_file的文件信息，repr多用于调试,将对象转化为供解释器读取的形式
print(">>>>in_file=",repr(in_file))
#将in_file的内容读取并赋值给indata，此时应为字符串类型
indata = in_file.read()
#打印from_file即in_file的数据长度
print(f"the input file is {len(indata)} bytes long")
#判断to_file文件是否已经存在
print(f"does the output file exist? {exists(to_file)}")
#提示已经可以进行操作或者ctrl+c取消
print("ready, hit return to confinue, ctrl-c to abort.")
#输入任意值，回车进行下一步,作用为暂停，也可以赋值。
input()
#打开to_file，w为写入参数
out_file = open(to_file, 'w')
#写入write，值为indata
out_file.write(indata)

print("alright,all done.")
#执行完毕后，关闭两个文件
out_file.close()
in_file.close()