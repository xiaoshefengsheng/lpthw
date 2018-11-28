# #a是一个列表，然后x是计算列表元素的长度，y初始为0
# a =('php', 'nginx', 'tomcat')
# x = len(a)
# y = 0
# #执行循环，当y在x的整数列表中，则输出a[y]+"=yes",且赋值给b，打印b,不换行. 然后y+1
# for y in range(x):    #range(start, stop[, step]) range语法,开始,结束,步长默认1
    # b = (a[y]+"=yes")
    # print(b, end = ' ')
    # y += 1

#定义三个列表 the_count, fruits, change 
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
#for循环第一个列表the_count数据并打印
# this first kind of for-loop goes through a list
for number in the_count:	
	print(f"this is count {number}")
#for循环fruits数据并打印	
#same as above
for fruit in fruits:
	print(f"a fruit of type: {fruit}")
#for循环change混合列表并打印	
#also we can go through mixed lists too
#notice we have to use {} since we don't know what's in items
for i in change:
	print(f"i got {i}")
#建立一个列表变量，赋值为空	
#we can also build lists, first start with an empty one 
elements = []
#for 循环0-5,append添加0-5的数据到elements列表中
# then use the range function to do 0 to 5 counts
for i in range(0, 6):   #range(0, 6)不包含最后一个数6
	print(f"adding {i} to the list.")
	#append is a function that lists understand
	elements.append(i)
#打印新的elements列表的数据i。此时的i和上面不是一个变量了。	
#now we can print them out too
for i in elements:
	print(f"element was: {i}")


