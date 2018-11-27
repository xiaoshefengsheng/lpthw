people = 20
cats = 30
dogs = 15

#条件为真，执行打印，使用布尔表达式可以很明确看出if语句是根据布尔值决定是否执行
if not False:
#条件为真，执行打印
#if people < cats:
	print("too many cats! the world is doomed!")
#条件为真，执行
if True or False:
#条件为假，不执行打印	
#if people > cats:
	print("not many cats! the world is saved!")
#条件为假，不执行打印
if people < dogs:
	print("the world is drooled on!")
#条件为真，执行打印	
if people > dogs:
	print("the world is dry!")
	
#dogs = dogs + 5 ，值为20	
dogs += 5
#条件为真，执行打印
if people >= dogs:
	print("people are greather than or equal to dogs.")
#条件为真，执行打印	
if people <= dogs:
	print("people are less than or equal to dogs.")
	
#条件为真，执行打印	
if people == dogs:
	print("people are dogs.")
	
#if执行了and语句，为真就打印第二行代码，为假就执行False为空。
#if语句缩进是区分层级，不缩进就会直接执行print语句，没有判断了。	
#+=是一个递增运算符，x += 1等同于 x = x + 1
#if语句可以使用布尔表达式的真假，确定是否执行下一行语句。