#定义add加法函数
def add(a, b):
	print(f"adding {a} + {b}")
	return a + b
#定义减法subtract函数	
def subtract(a, b):
	print(f"subtracting {a} - {b}")
	return a - b
#定义multiply乘法函数	
def multiply(a, b):
	print(f"multiply {a} * {b}")
	return a * b
#定义除法divide函数
def divide(a, b):
	print(f"divide {a} / {b}")
	return a / b
	
print("let's do some math with just functions!")
#调用上面定义的加减乘除的函数处理数据
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
#打印结果，age=35,height=74,weight=180,iq=50
print(f"age: {age}, height: {height}, weight: {weight}, iq: {iq}")


# a puzzle for the wxtra credit, type it in anyway.
print("here is a puzzle.")
#组合函数进行计算，先运算最内部的。
#先计算divide(iq, 2)其实是50/2=25
#计算multiply(weight , 25)即180*25=4500
#处理subtract(height ,4500)即74-4500= -4426
#处理add(age, -4426)即35+ -4426=-4391
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("thar becomes: ", what, "can you do it by hand?")
	