#前三条为print命令。练习了转义符\，\n \t \' \\等。
print("let's practice everything.")
print('you\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')
#赋值变量poem为多行字符串。 并使用\n \t 等换行或缩进每行。
poem = """
\tthe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
#print分隔符~字符串，以及变量poem多行字符串。
print("----------")
print(poem)
print("----------")

#five变量赋值为数学运算，结果为5
five = 10 - 2 + 3 - 6
print(f"this should be five: {five}")
#定义secret_formula函数，处理参数started,通过运算获得几个变量，return返回几个变量值
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
#赋值变量start_point值为10000，变量beans,jars,crates通过调用函数secret_formula处理start_point获得返回的列表值，按序赋值给变量
start_point = 10000
beans, jars, crates = secret_formula(start_point)

#remeber that this is another way to format a string
#在print函数中直接对字符串进行format(start_point)，值会传入字符串的{}中。
print("with a starting point of: {}".format(start_point))
#it's just like with an f"" string
#使用f格式化字符串，导入变量，变量用{}括住。
print(f"we'd have {beans} beans, {jars} jars, and {crates} crates.")
#赋值变量start_point等于start_point / 10 为1000
start_point = start_point / 10

print("we can also do that this way:")
#赋值变量formula为调用函数secret_formula(start_point)获得的值，是一组列表值
formula = secret_formula(start_point)
#this is an easy way to apply a list to a format string
#可以在print函数中直接调用format结合{}，按序填入列表值。
print("we'd have {} beans, {} jars, and {} crates.".format(*formula))