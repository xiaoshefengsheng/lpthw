# 如ex11一样，age可以用int转换为整数类型.
age = int(input("how old are you? "))
# 在input中使用f格式化字符串，引用变量是没问题的，这可以更方便的提示。
height = input(f"you are {age} ,nice .how tall are you? ")
weight = input("how much do you weight? ")

print(f"so, you're {age} old, {height} tall and {weight} heavy.")

# 类似的例子如游戏创建人物时候的问题。我们可以直接在提示中就输出已经输入的变量，而不用单独print。
name = input("your name ?")
job = input(f"hi {name} ,welcome . what are you job?")

print(f" so, {name} ,your job is {job} ,and your age is {age}")

