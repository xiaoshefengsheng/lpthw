##Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## ??dog is-a animal  
class Dog(Animal):
	
	def __init__(self, name):
		## ?? dog has-a name
		self.name = name
		
## ??  is-a
class Cat(Animal):
	
	def __init__(self, name):
		## ?? has-a
		self.name = name
		
## ?? person is-a object
class Person(object):
	
	def __init__(self, name):
		## ??  has-a
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
		
## ?? employee is-a person
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?  has-a name
		super(Employee, self).__init__(name)  #子类调用父类时使用super(子类名,self).方法名(参数),子类调用person的name，因为这里本来没有定义name这个东西
		## ??  employee has-a salary
		self.salary = salary
	
## ?? fish is-a object
class Fish(object):
	pass

##?? salmon is-a fish
class Salmon(Fish):
	pass
	
## ?? halibut is-a fish 
class Halibut(Fish):
	pass
	
	
## rover is-a Dog
rover = Dog("Rover")

## ??  satan is-a cat
satan = Cat("Satan")

## ??  mary is-a person
mary = Person("Mary")

## ??  mary has-a pet ,pet has-a name satan 
mary.pet = satan

## ??  frank is-a employee, frank has-a 120000 salary
frank = Employee("Frank", 120000)

## ??  frank has-a pet,pet has-a name rover
frank.pet = rover

## ??  把 flipper 设为fish类的实例
flipper = Fish()

## ?? 把crouse 设为salmon三文鱼的实例 
crouse = Salmon()

## ?? 把 harry设为halibut大比目鱼的一个实例 
harry = Halibut()

# 从整个计算机科学的角度来说，对象是对客观事物的抽象，类是对对象的抽象，大类是对小类的抽象。类和对象都是一种抽象的数据类型。

# 对象(Object)：是指在应用问题中出现的各种实体、事件和规格说明等，它是由一组属性和在这组值上的一组服务（这里的服务指的是操作，就是我们写在类里的函数所提供的功能）构成的，其中属性值确定了对象的状态。

# 类(Class)：把具有相同属性和服务的对象归到同一类，而把一个类中的的每一个对象称为该类的一个实例(Instance)，它们具有相同的服务。

# 继承：面向对象方法最有特色的方面。

# 继承性(Inheritance)是指，在某种情况下，一个类会有“子类”。子类比原本的类（称为父类）要更加具体化、定制化。