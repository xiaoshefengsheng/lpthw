#选择打开哪扇门的游戏，门后面是未知的黑暗世界~~
print("""you enter a dark room with two doors.
do you go thriygh door #1 or door #2?""") 
#打开哪扇门？请输入，赋值door变量为用户输入的值。此处不限制输入的数据，默认类型为str
door = input("> ")
#如果输入的是字符串1，则执行下面的代码块
if door == "1":
	print("there's a giant bear here eating a cheese cake.")
	print("what do you do?")
	print("1. take the cake.")
	print("2. scream at eht bear.")
#执行代码块中，使用input函数接受用户输入	
	bear = input("> ")
#代码块中嵌套了if语句，如果输入字符串1，执行第一个语句，同理2为第二个语句，其他为最后
	if bear == "1":
		print("the bear eats your face off. good job!")
	elif bear == "2":
		print("the bear eats your legs off. good job!")
	else:
		print(f"well,doing {bear} is probably better.")
		print("bear runs away.")
#主语句的第二个判断，如果输入的为2，则执行以下代码块		
elif door == "2":
	print("you stare into the endless abyss at cthulhu's retina.")
	print("1. blueberries.")
	print("2. yellow jacket clothespins.")
	print("3. understanding revolvers yelling melodies.")
#代码块中接收输入参数	
	insanity = input("> ")
#主if语句中的嵌入if语句，输入1或者2都会执行第一个语句。输入其他，则到else	
	if insanity == "1" or insanity =="2":
		print("your body survives powered by a mind of jello.")
		print("good job!")
	else:   
		print("the insanity rots your eyes into a pool of muck.")
		print("good job!")
#主if语句，如果不符合条件1和2，则输入其他任何参数都会跳转到else		
else:
	print("you stumble around and fail on a knife and die. good job!")