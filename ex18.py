#本例学的是定义函数的方法
#this one is like your scripts with argv
#定义函数print_two,函数处理对象为*args，赋值变量为两个参数
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

#ok, that *args is actually pointless, we can just do this
#对比上面，可以看出，可以直接定义函数时设定接收两个参数
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
	
#this just takes one argument
#此处设置仅一个参数
def print_one(arg1):
	print(f"arg1: {arg1}")
	
#this one takes no arguments
#此处定义函数不要参数
def print_none():
	print("i got nothin'.")

#跟print,input函数一样，直接使用函数（对象），如下直接调用了上面自定义的函数方法。	
print_two("xiao","she")
print_two_again("xiao","she")
print_one("first!")
#此处调用的时候，如果有参数对象就会报错。
print_none()
