#赋值ten_things变量为字符串
ten_things = "apples oranges crows telphone light sugar"
#这个列表中没有10个元素，可使用代码修改下并实现。
print("wait there are not 10 things in that list . let's fix that.")
#定义stuff变量，赋值为ten_things的split分割方法，使用空格分割为列表
stuff = ten_things.split(' ')
print(stuff) #根据输出结果，可以看出stuff是一个列表。
print(type(stuff))  #使用type函数看出，stuff是一个list.
#定义more_stuff变量，赋值为一个列表。
more_stuff = ["day", "night", "song", "frisbee", "corn", "banana", "girl", "boy"]
#执行while循环，条件为len(stuff) != 10，即用len函数查看stuff长度为多少，如果不等于10的时候为真，执行代码块
while len(stuff) < 10:
	next_one = more_stuff.pop()  #定义变量next_one，赋值为more_stuff.pop(),即对more_stuff执行pop函数，默认为抓取more_stuff的最后一个元素,抓取后原list值减少一个
	print("adding:", next_one)  #打印取到的元素值。
	stuff.append(next_one)  #执行stuff.append(next_one) ,将元素添加到stuff列表中
	print(f"there are {len(stuff)} items now.") #打印len(stuff)，知道执行一次循环后的stuff长度。
	
print("there we go: ", stuff)  #打印stuff的值，此时应该是10个元素了

print("let's do some things with stuff.")  

print(stuff[1])  #输出stuff的第二个元素，因为默认从0开始
print(stuff[-1]) # whoa! fancy 输出最后一个元素
print(stuff.pop())  #取出stuff的最后一个元素并打印
print(' '.join(stuff)) #what? cool! 对stuff中每个元素添加空格分割
print('#'.join(stuff[3:5])) #super stellar! 对索引3至4取值打印，并添加'#'分割