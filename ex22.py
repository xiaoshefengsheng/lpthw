#print函数，括号中接收处理对象或者参数，在""或''中包含的数据就是字符串。""""""三个引号可以包含更多的注释，且可以随时换行。 '#'字符后面的是注释，不会被运行
print("Hello world@") 
f = """第一行 first
第二行 second
第三行 third
"""
print(f)
#双引号包含的为字符串， 后面的则会直接运行
print("hens", 25 + 30 /6) #输出为：hens 30.0 运算结果为浮点数float
print("is it greater?",5 > -2)#输出为：is it greater? Flase 此处结果为布尔值
#关于数学运算符： + 加，- 减，*乘，/除，%除法取余，//除法取整，**幂方
#关于数字逻辑运算：> 大于，<小于,>=大于等于，<=小于等于，=等于，!=不等于，<>也是不等于
#print括号中未被引号的变量，会输出变量值,如下
cars = 100
print("there are ", cars ."cars available."#输出 there are 100 cars available
#通过f方法格式化函数内容，花括号括住的变量会执行输出值。
print(f"there are {cars} cars available")
#另外也可以用format方法处理变量，格式化为字符串。
f = False #此处为bool布尔值
format(f) #此处为字符串str
#也可以用一个字符串使用format方法，使布尔变量被格式化为字符串，{}为变量位置
x = "this {} is bool."
print(x.format(f)) 
print("this  {} is bool".format(f))#输出 this False is bool. 这就在字符串里了。
#字符串组合
a = "chen"
b = "rui"
c = "ning"
print(a + b + c) # chenruining
print(a * 3) #chenchenchen

#\转义符， \n换行，\t一个制表符，\\转义\。 在字符串中可以直接使用转义符。

age = input() #接收用户的输入
age = int(input()) #将输入转换为int值，也可以转换为str等
print(f"so ,you are {age} old") #再使用f方法输出变量在字符串中
#赋值变量的时候，在input中的提示字符，可以直接引用上面的变量age
height = input(f"you are {age} old,nice ,how tall are you?")

#引入argv模块，可以方便的在执行脚本时，直接跟参数。
from sys import argv #就是从sys库中导入argv模块到脚本中。 #import可以很方便的引用别人编写好的库函数。 argv是一个可以接收脚本后参数的库模块。利用这种方法，可以在脚本后跟要处理的文件或参数，这样就实现了用脚本处理文件，甚至是大量的文件。
repr(argv) #输出argv引用的具体参数，repr可用于debug调试函数和脚本
type(argv) #输出argv的文件类型，也是用于debug。

#结合f文本格式化方法和argv模块，可以在打印字符串中输出argv参数的值，也可以在input()中用f格式化字符串方法，把argv参数作为提示符输出。 f格式化字符串时，变量要用花括号括起来，这样才能识别。
open(file_name) #open函数可以打开一个文本文件
file_name.read() #.read方法可以读取打开的文本文件
print(file_name.read()) #打印读取的文件内容到屏幕上
file_name1 = 
file_name.truncate() #.truncate()是从指定位置截断文件，如创建新文件后终端，则文件为空文件。
file_name.write("写入的内容") #向文本文件写入内容或者变量等
file_name.close()#关闭文件

from os.path import exists #从os.path库中导入exists模块，该模块可以判断文件是否存在
exists(data) #判断变量是否存在。则输出应为布尔值bool
len(data) #len函数可以判断data数据或变量的数据长度

#def即define定义函数，function1函数名，arg1处理对象或参数，:为语法
def function1(arg1): 
	print(f"arg1: {arg1}") #调用函数后，执行的操作
function1(arg1) #函数调用方法
#如下所示，函数可以直接调用数据，也可以定义变量后处理，也可以运算变量，只要参数符合规则即可。
def function2(arg2,arg3):
	print(f"arg2: {arg2}")
	print(f"arg3: {arg3}")
function2(10,20)
a = 30
b = 40
function2(a,b)
function2(10+30,20+40)
function2(a+10,b+20)

file.read() #读取文本文件
file.seek(0) #倒带定位到0，初始位置
file.readline() #逐行读取
#def函数，一般是需要return返回值。return是定义函数的关键字。
def add(a,b):   #定义函数add，参数a,b两个。
	print(f"adding {a} + {b}") #此处为字符串，直接输出了变量的值
	return a + b #此处进行计算，调用函数后会输出最终结果
add(10,20)  #输出结果为30
#1、 主要学习了print, format字符串结合变量，结合input等。
#2、 学习了argv模块，该模块允许脚本后跟参数直接处理。 参数可以是文件。
#3、 def定义函数，学习自定义函数，以及函数的调用