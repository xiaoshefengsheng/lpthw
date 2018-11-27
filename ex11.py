# 练习input函数的使用，可以接收用户的输入值。
print("how old are you?", end=' ')
# 接收用户的输入，并把input的字符串值传给int函数，转换为整数类型
age = int(input())
# 通过repr函数，可以复现并输出上面的age变量被赋予的什么值，是字符串还是整形或者浮点数。也可以使用type函数，直接看到告知的类型。
print(type(age))
print(">>> age=", repr(age))
print("how tall are you ?", end=' ')
height = input()
print("how much do you weight?", end=' ')
weight = input()

#使用f格式化字符串，可以输出变量的值。
print(f"so, you are {age} old, {height} tall, {weight} weight.")
