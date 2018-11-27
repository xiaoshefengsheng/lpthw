from sys import argv
# 同上一个例题一样，argv赋予到几个变量上，外面输入命令是就需要输入几个，此处其实是一个，脚本默认肯定是有的。
script, user_name = argv
# 定义一个提示符的变量，方便下面的提示展示，可以使用f格式化来组合该变量的使用，如把脚本名和上面的用户名变量定义在下面提示符变量里
prompt = f"{script}-{user_name} > "

print(f"hi {user_name} , i'm the {script} script.")
print("i'd like to ask you a few questions.")
print(f"do you like me {user_name}?")
likes = input(prompt)

print(f"where do you live {user_name}?")
lives = input(prompt)

print(f"how old are you {user_name}?")
age = input(prompt)
# 此处格式化里面包含了一个int函数，将输入的age值转换为整数类型。 请注意，f格式化字符串后，识别的是字符串中的花括号{}，函数要写里面
print(f"you are int{int(age)}.")

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
alright, so you age is {age},you said {likes} about liking me .
you live in {lives}. not sure where that is .
and you have a {computer} computer. nice.
""")