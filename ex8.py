# 定义一个变量，赋值为4个可接收格式化参数的空值，如果变量只给三个{}参数，而下面的参数引入了4个值，就只打印从左往右的前三个。
formatter = "{} {} {} {} "
# 执行format方法的时候从左往右。
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
# 参数为布尔值，format后变为字符串
print(formatter.format(True, False, False, True))
# 直接打印布尔值，也不会报错，但是修改比如False为false就会报错，报错信息为变量没有定义。 也就是说如果按布尔值变量打印无问题，按正常变量打印的话，需要赋值。 按字符串的话，需要加双引号。
print(True, False, False, True)
# 此处格式化变量formatter,该变量的赋值已设置双引号，所以按字符串“｛｝”格式化了。
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "try you",
	"own text here",
	"maybe a pome",
	"or a song about fear"
))