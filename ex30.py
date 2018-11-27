#赋值三个变量
people = 30
cars = 40
trucks = 15

#if语句判断条件是否为真，为真则执行所属的代码块，if语句结束。为假则处理下一个判断
if cars > people:
	print("we should take the cars.") #上面条件为真，执行打印
elif cars < people:  #因if语句已判断结束，上面的条件为真，则此处不再判断
	print("we should not take the cars.")
else:  #上面为真，此处不判断
	print("we can't decide.")
#if判断为假，执行下一个判断	
if trucks > cars:
	print("that's too many trucks.")  #条件为假，不执行，执行下一个判断
#上面为假，此处进行判断，为真，则执行
elif trucks < cars:
	print("maby we could take the trucks.")  #执行
#上面已经判断结束，此处不再判断，若上面条件均为假，则执行此操作
else:
	print("we still can't decide.")
#执行if语句判断	
if people > trucks:
	print("alright,let's just take the trucks.")  #条件为真，执行代码块
else:
	print("fine, let's stay home then.")