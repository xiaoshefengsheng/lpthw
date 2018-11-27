# 赋值变量types_of_people 值为10
types_of_people = 10
# 使用f-string格式化字符串，使其中的变量{types_of_people}可以被引用。
x = f"there are {types_of_people} types of people."
#赋值“binary” 给变量binary
binary = "binary"
do_not = "don't"
# 使用f-string格式化字符串，使其中的变量{binary} {do_not}可以被引用。
y = f"those who know {binary} and those who {do_not} ."
#打印变量
print(x)
print(y)
#打印格式化的字符串，{x}{y}都可以被引用。
print(f"i said: {x}")
print(f"i aslo said : '{y}'")
#赋值变量hilarious 为布尔值False。
hilarious = False
#赋值变量 joke_evaluation 值为字符串，{}支持变量对象的引入。
joke_evaluation = "isn't that joke {} so funny?! "
print(joke_evaluation)
# 打印变量，并使用format字符串处理方法，对变量hilarious对象布尔值格式化处理为字符串。
print(joke_evaluation.format(hilarious))
