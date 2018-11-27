#导入argv库
from sys import argv
#设置两个参数对象
script, input_file = argv
#定义函数print_all,处理对象f，使用read方法查看f,为清晰看到处理过程，增加了两行print("<<<")调试
def print_all(f):
	print(">>> print_all: f=", f)
	print(f.read())
	print("<<< print_all: f=", f)
#定义函数rewind倒带，使用f的seek方法，查找行，设置为0,即回到初始位置	
def rewind(f):
	f.seek(0)
	
#定义函数print_a_line,处理对象为line_count,f,两个对象.处理方法为打印第一个对象，第二个对象用readline方法处理打印具体行,可以定位到上次执行完的位置,逐行打印一次,end=""去除多的换行
def print_a_line(line_count, f):
	print(">>> 开始")
	print(line_count, f.readline(), end="")
	print("<<< 结束")
#定义变量current_file为最上方的参数变量文件
current_file = open(input_file)
#打印一行提示
print("first let's print the whole file:\n")
#执行函数print_all,参数current_file,也就是参数里的文件
print_all(current_file)
#打印一行提示
print("now let's rewind, kind of like a tape.")
#执行rewind函数，处理参数current_file,执行的是seek方法,无返回值，可以定位文件读取的位置
rewind(current_file)
#打印一行提示
print("let's print three lines:")
#此处定义变量current_line为1，简单的处理打印的行号
current_line = 1
#执行print_a_line函数，行号初始为1，然后第二个参数使用readline方法，逐行读取
print_a_line(current_line, current_file)

current_line = current_line + 1
#current_line加1，计算后为2，第二个参数执行的是print_a_line里的readline方法，打印的是第二行，与前面的current_line变量值无关
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

