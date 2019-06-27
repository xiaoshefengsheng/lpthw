'''
for 变量 in 序列：
	执行的代码块
'''

# list01 = ['joe', 'susan', 'jack', 'tom']
# #遍历列表
# for i in list01:   #遍历list01这个列表，将列表中的元素依次赋值给变量i
	# print(i)    #输出变量i,直到将所有的元素遍历完毕，停止遍历

	#用while遍历列表
# i = 0
# while i < len(list01):
	# print(list01[i])
	# i += 1
	
# favorite_places = {'张三':['上海','北京','深圳'],'李四':['张家界','九寨沟','鼓浪屿']}
# name = input('请输入姓名：')
# for i in favorite_places:
	# #print(i)
	# if name == i:
		# print(favorite_places[name])  #通过访问字典的下标，访问字典的值
		
# list01 = ['joe', 'susan', 'jack', 'tom']
# for i in list01:
	# if i == 'susan':
		# #break   #终止循环
		# #continue  #中止当前循环，开始下一次循环
		# pass #表示什么操作都没有，占位
	# print(i)
	
	
# favorite_places = {'张三':['上海','北京','深圳'],'李四':['张家界','九寨沟','鼓浪屿']}
#name = input('请输入姓名：')
# for i in favorite_places.values():
	# print(i)
	#if name == i:
	#	print(favorite_places[name])  #通过访问字典的下标，访问字典的值
# print(favorite_places.items())
# for i in favorite_places.items():
	# print(i)
	
# for k,v in favorite_places.items():
	# print(k,v)
#99乘法表	
# for x in range(1,10):
	# for y in range(1,10):
		# z = (x * y)
		# print("%s*%s=%s" % (x, y, z),end = ' ')

i = 1
while i <10:
	#print(i)
	j = 1
	while j <=i:
		print("%s*%s=%s" % (i, j, (i * j)),end = '\t')
		j += 1
	i += 1
	print()
	



