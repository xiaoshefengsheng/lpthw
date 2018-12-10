"""
'关键字'
and    逻辑与    				True and False == False
as     with-as 语句的一部分		with X as Y: pass
assert 断言（确保）某东西为真	assert False, "Error!"
break	立即停止循环			while True: break
class 	定义类					class Person(object)
continue 停止当前循环的后续步骤，再做一次循环		while True: continue
def 	定义函数				def X(): pass
del    从字典中删除				del X[Y]
elif	else if 条件			if: X; elif: Y; else: J
else	else条件				if: X; elif: Y; else: J
except	如果发生异常，运行此处代码	except ValueError, e: print(e)
exec	将字符串作为python脚本运行	exec 'print("hello")'
finally	不管是否发生异常，都运行此处代码	finally: pass
for 	针对物件集合执行循环	for X in Y: pass
from	从模块中导入特定部分	from x import Y
global  声明全局变量			global X
if		if条件					import os
in 		for 循环的一部分，也可以X是否在Y中的条件判断 for X in Y: pass 以及 1 in [1] == True
is      类似于==，判断是否一样	1 is 1 == True
lambda	创建短匿名函数			s = lambda y: y ** y; s(3)
not 	逻辑非					not True == False
or		逻辑或					True or False == True
pass	标识空代码块			def empty(): pass
print	打印字符串				print('this string')
raise	出错后引发异常			raise ValueError("No")
return  返回值并退出函数		def X: return Y 
try		尝试执行代码，出错后转到except	try: pass
while	while循环				while X: pass
with	将表达式作为一个变量，然后执行代码块	with X as Y: pass
yieid	暂停函数，返回到调用函数的代码中	def X(): yield Y; X().next()
'数据类型'
True    布尔值“真”		True or False == True
False    布尔值"假"		False and True == False
None	 表示"不存在"或者“没有值”	X = None
bytes	 字节串存储，可能是文本，PNG图片、文件等	X= b'hello;"
strings  存储文本信息			X = ’hello'
numbers  存储整数				i = 100
Floats	 存储十进制指数			i = 10.389
lists	 存储列表				j = [1, 2, 3, 4]
dicts	 存储键值映射			e = {'x': 1,'y': 2}

'字符串转移序列'
\\		反斜杠
\'		单引号
\"		双引号
\a		响铃
\b 		退格符
\f 		表单填充符
\n 		换行符
\r  	回车
\t  	制表符
\v 		垂直制表符

'老式字符串格式'
%d 		十进制整数（非浮点数）	"%d" % 45 == '45'
%i 		和%d一样				"%i" % 45 == '45'
%o 		八进制数				"%o" % 1000 == '1750'
%u 		无符号整数				"%u" % -1000 == '-1000'
%x 		小写十六进制			"%x" % 1000 == '3e8'
%X		大写十六进制数			"%X" % 1000 == '3E8'
%e 		指数表示，小写e			"%e" % 1000 == '1.000000e+03'
%E 		指数表示，大写E			"%E" % 1000 == '1.000000E+03'
%f 		浮点实数				"%f" % 10.34 == '10.340000'
%F 		和%f一样				"%F" % 10.34 == '10.340000'
%g 		%f和%e中较短的一种		"%g" % 10.34 == '10.34'
%G 		和%g一样，但是是大写	"%G" % 10.34 == '10.34'
%c 		字符格式				"%c" % 34 == '"'
%r 		repr格式（调试格式）	"%r" % int == "<type 'int'>"
%s 		字符串格式				"%s there" % 'hi' == 'hi there'
%%		百分号自身				"%g%%" % 10.34 == '10.34%'
'运算符'
+		加			2 + 4 = 6
-		减			2 - 4 = -2
* 		乘			2 * 4 = 8
**		幂			2 ** 4 = 16
/ 		除			2 / 4 = 0.5
//		整除		2 // 4 = 0
%		字符串翻译，或者求余数		2 % 4 = 2
<		小于		4 < 4 == False
>		大于		4 > 4 == False
<= 		小于等于	4 <= 4 == True
>= 		大于等于	4 >= 4 == True
== 		等于		4 == 5 == False
!=		不等于		4 != 5 == True
()		括号		len('hi') == 2
[]		方括号		[1, 3, 4] 
{}		花括号		{'x': 5, 'y': 10}
@		修饰器符	@classmethod
,		逗号		range(0, 10)
:		冒号		def x():
.		点			self.x = 10
= 		赋值		x = 10
;		分号		print('hi'); print('there')
+=		加后赋值	x = 1; x += 2
-= 		减后赋值	x = 1; x -= 2
*=		乘后赋值	x = 1; x *= 2
/= 		除后赋值	x = 1; x /= 2
//=		除后舍余并赋值		x = 1; x //= 2
%=		求余后赋值		x = 1; x %= 2
**=		求幂后赋值		x = 1; x **= 2
"""