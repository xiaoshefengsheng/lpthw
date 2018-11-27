print("How old are you?", end=' ')  #打印提示，end' '为输出空格
age = input()                       #input为支持用户输入函数
print("How tall are you?", end=' ') 
height = input()
print("How much do you weigh?", end=' ')
weight = input()
#print字符串，用f函数格式化字符串，支持{}中的变量输出
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
from sys import argv     #导入argv模块，支持用户脚本后直接跟参数
script, filename = argv  #第一个参数都是脚本名

txt = open(filename)      #赋值txt变量为打开filename

print(f"Here's your file {filename}:")  #使用f方法，使变量可以被输出
print(txt.read())  #打印txt的读取输出到屏幕

print("Type the filename again:") #提示语句
file_again = input("> ")  #在input函数中直接添加提示符或语句

txt_again = open(file_again)  #txt_again赋值为打开上面输入的文件

print(txt_again.read())  #输出文件的读取到屏幕


print("Let's practice everything.") #提示语句
#多行字符串，用""""""，中途可以随意换行，避免其中有关键字打断字符串
print("""You\'d need to know \'bout escapes 
      with \\ that do \n newlines and \t tabs.""")
#定义poem为多行字符串
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")  #打印分隔符字符串
print(poem)  #打印多行字符串
print("--------------")  #打印分隔符字符串


five = 10 - 2 + 3 - 6  #赋值five为 5
print(f"This should be five: {five}") #使用f方法打印 {five}变量
#定义函数secret_formula
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars + 100
    return jelly_beans, jars, crates   #返回三个值的列表


start_point = 10000
beans, jars, crates = secret_formula(start_point) #赋值前面三个变量为secrte_formula(start_point)的返回的值
print(type(secret_formula(start_point)))  #调试查看什么类型并打印输出到屏幕
# remember that this is another way to format a string
#format字符串，将返回值传入到{}中
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
#使用f方法将变量直接输出{beans}等
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")
#start_point赋值为原值/10
start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
print(type(formula)) 
# this is an easy way to apply a list to a format string
#将元组按序传入到{}中
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30
dogs = 15

#条件符合，打印输出,python3需要print(),不能少括号
if people < cats:
    print ("Too many cats! The world is doomed!")
#条件不符，不执行打印
if people > cats:
    print("Not many cats! The world is saved!")
#条件不符，不执行打印
if people < dogs:
    print("The world is drooled on!")
#条件符合，打印输出
if people > dogs:
    print("The world is dry!")

#下面的表达式也就是dog = dog + 5
dogs += 5
#条件符合，打印输出
if people >= dogs:
    print("People are greater than or equal to dogs.")
#条件符合，打印输出
if people <= dogs:
    print("People are less than or equal to dogs.")

#条件符合，打印输出
if people == dogs:
    print("People are dogs.")
