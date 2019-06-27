# def conver(a, b):
	# return print(b, a)

# aaa = 5
# bbb = 6
# print(id(aaa))
# print(id(bbb))
# #print(conver(aaa, bbb))
# c = conver(aaa, bbb)
# print(id(c))

# class Animal(object):
	# pass

# ## ??dog is-a animal  

# class Dog(Animal):
	
	# def __init__(self, name):
		# ## ?? dog has-a name
		# self.name = name

# ## rover is-a Dog
# rover = Dog("Rover")



# a = "hello world!"
# print(a[::-1])
# strlen = len(a)
# for i in range(1,strlen+1):
	# print(a[-i],end='')
	
# def getinfo(name, address):
	# print('大家好我是%s,我来自%s' % (name,address))

# address=input('请输入来自哪里：')
# name=input('请输入姓名：')
# getinfo(name,address)

# var = int(input("输入数："))
# # print(bool(var))
# print(var + 1)


a = 2
b = a
a = 3
print(id(a))
print(id(b))
print(a)
print(b)

lista = [1, 2]
listb = lista
lista[0] = 3
print(id(lista))
print(id(listb))
print(lista,listb)











