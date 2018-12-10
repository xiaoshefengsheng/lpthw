#导入exit模块
from sys import exit
#定义函数gold_room
def gold_room():   #充满金子的房间
	print("this room is full of gold. how much do you take?")
	#提示输入
	choice = input("> ")
	if "0" in choice or "1" in choice:   #如果输入的数字带1或者0
		how_much = int(choice)  #赋值how_much为 int(choice)
	else:   #如果choice不含1和0，则调用dead函数，结束游戏
		dead("man, learn to type a number.")
#上面的if判断输入值后，赋值了变量how_much为整数。下方if为单独的代码块，对how_much再判断	
	if how_much < 50:   #小于50，则输出胜利，并退出。
		print("nice, you're not greedy, you win!")
		exit(0)
	else:    #如变量的数值太大，则输出 dead函数，并告知因为太贪婪
		dead("you greedy bastard!")
#定义函数bear_room，即有熊的房间		
def bear_room():
	print("there is a bear here.")
	print("the bear has a bunch of honey.") 
	print("the fat bear is in front of another door.")
	print("how are you going to move the bear?")
	bear_moved = False    #赋值变量bear_moved初始False即不移动
	#执行while True无限循环，利用里面调用的函数结束循环
	while True:
		choice = input("> ")  #输入要进行的操作
		
		if choice == "take honey":   #if 移动蜂蜜 take honey 
			dead("the bear looks at you then slaps your face off")  #dead，失败
#嘲弄熊,并在第一次循环时赋值bear_moved为True，而后面的循环因为这个elif条件为假就不执行了
		elif choice == "taunt bear" and not bear_moved:  
			print("the bear has moved from the door")
			print(bear_moved, "you can go through it now")
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:  #再次输入taunt bear就会失败dead
			print(bear_moved)  #调试语句，查看下当前的bear_moved值
			dead("the bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:  #输入open door，调用gold_room函数
			gold_room()
		else:  #输入不正确，则输出以下内容，并再次循环
			print("i got no idea what that means.")
			
#定义函数cthulhu_room即邪神的房间			
def cthulhu_room():
	print("here you see the great evil cthulhu.")
	print("he, it, whatever stares at you and you go insane.")
	print("do you flee for your life or eat your head?")
#输入选择的内容	
	choice = input("> ")
#输入flee逃命，则重新开始，输入head脑袋，则失败。 否则继续循环	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("well that was tasty!")
	else:
		cthulhu_room()
#定义dead失败函数，输出dead引入的参数即失败原因，并exit退出。		
def dead(why):
	print(why, "good job!")
	exit(0)
#定义start开始函数，选择哪一个门
def start():
	print("you are in a dark room.")
	print("there is a door to your right and left.")
	print("which one do you take?")
#输入选择的内容	
	choice = input("> ")
#如果选择left,则去往有熊的房间。 选择right,则去往邪神的房间。 其他选择则失败。	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("you stumble around the room until you starve.")
#执行start()		
start()
#本章代码较多，可以分割为小代码块，先确定骨架，再细化代码。 #即先确定所有函数，然后再给函数增加代码。