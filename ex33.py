#while 后面跟的语句，一定是逻辑可判断True或者False的才能执行。
# i = 0
# numbers = []

# while i < 6:  #当i < 6为真，执行下方代码块
	# print(f"at the top i is {i}")  #打印循环开始的i的值
	# numbers.append(i)  #在列表最后追加一个元素
	
	# i = i + 1   #对变量i运算为i + 1
	# print("numbers now: ", numbers)  #打印现在的列表值
	# print(f"at the bottom i is {i}")  #打印运算后的i的值
	
# #打印numbers中的每一个值，print默认换行，可以增加end = ' '不换行。	
# print("the numbers: ")
# for num in numbers:
	# print(num)

#---------------for循环写法-------------
# i = 0
# numbers = []
# #当使用for循环，且已知的范围时，它会根据范围做循环，与下面的i递增规则无关系
# for i in range(0, 6):  #当i < 6为真，执行下方代码块
	# print(f"at the top i is {i}")  #打印循环开始的i的值
	# numbers.append(i)  #在列表最后追加一个元素
	
	# i = i + 2   #对变量i运算为i + 2
	# print("numbers now: ", numbers)  #打印现在的列表值
	# print(f"at the bottom i is {i}")  #打印运算后的i的值
	
# #打印numbers中的每一个值，print默认换行，可以增加end = ' '不换行。	
# print("the numbers: ")
# for num in numbers:
	# print(num, end = ' ')
	
#---这是使用导入argv模块的方法,可以直接在脚本名后跟两个参数执行循环。---
# from sys import argv	
# script, a, b = argv
# a = int(a)
# b = int(b)
# def while1(a, b):
	# i = 0
	# numbers = []
	# while i < a:  #当i < 6为真，执行下方代码块
		# #print(f"at the top i is {i}")  #打印循环开始的i的值
		# numbers.append(i)  #在列表最后追加一个元素
		
		# i = i + b   #对变量i运算为i + 1
		# #print("numbers now: ", numbers)  #打印现在的列表值
		# #print(f"at the bottom i is {i}")  #打印运算后的i的值
		
	# #打印numbers中的每一个值，print默认换行，可以增加end = ' '不换行。	
	# print("the numbers: ")
	# for num in numbers:
		# print(num)
		
# while1(a, b)



#定义一个函数，可以在其他脚本或终端中引用。import ex33 ,然后ex33.while1(10, 2)使用
def while1(a, b):
	i = 0
	numbers = []
	while i < a:  #当i < a为真，执行下方代码块，a为最大循环
		#print(f"at the top i is {i}")  #打印循环开始的i的值
		numbers.append(i)  #在列表最后追加一个元素
		
		i = i + b   #对变量i运算为i + b ，b相当于步长
		#print("numbers now: ", numbers)  #打印现在的列表值
		#print(f"at the bottom i is {i}")  #打印运算后的i的值
	print(numbers)	
	#打印numbers中的每一个值，print默认换行，可以增加end = ' '不换行。	
	#print("the numbers: ")
	#for num in numbers:
	#	print(num)
