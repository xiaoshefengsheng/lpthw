import sys  #导入sys库
script, encoding, error, languages = sys.argv  #赋值三个变量参数给sys.argv模块

#定义主函数main,对参数进行处理。 参数依次为:文件、编码类型、错误处理
def main(language_file, encoding, errors):
	print(">>>> in main ",repr(language_file), encoding, errors)
	line = language_file.readline()  #赋值变量line为逐行读取文件
	print(">>>line:", line)
	if line:   #此处if语句的条件是，当line可读取到内容为真，继续执行，读取不到则停止
		print_line(line, encoding, errors) #调用下方的函数处理文件、编码和错误参数
		print(">>>> main again")
		return main(language_file, encoding, errors) #调用main函数处理参数，此处算是自我循环，只有当if为假就停止
	print("<<<< main exit")	
#定义函数print_line		
def print_line(line, encoding, errors):
	print("line:", repr(line), encoding, errors)
	next_lang = line.strip()  #.strip的作用是去除开头和结尾的空行或换行符
	raw_bytes = next_lang.encode(encoding, errors = errors) #对字符串编码为字节串
	cooked_string = raw_bytes.decode(encoding, errors = errors) #对字节串解码为字符串
	
	print(raw_bytes, "<===>", cooked_string) #打印上面的两个变量，可看到一致
	print("print_line done")
#赋值变量languages为使用utf-8编码，打开某个文件	
#languages = open("languages.txt", encoding = "utf-8")
#也可以直接在参数上赋值要打开的文件，以后就可以用脚本处理其他文本文件
languages = open(languages, encoding = "utf-8")
#调用main函数处理文件，函数自带循环，从终端可看到处理结果，添加调试代码也可
main(languages, encoding, error)