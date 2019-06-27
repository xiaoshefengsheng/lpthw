类(class): 告诉python创建新类型的东西
对象(object): 两个意思，即基本的东西，或者某样东西的实例
实例(instance): 这是让python创建一个类时得到的东西
def: 这是在类里面定义函数的方法
self: 在类的函数中，self指代被访问的对象或者实例的一个变量。
继承(inheritance): 指一个类可以继承另一个类的特性，和父子关系类似
组合(composition): 指一个类可以将别的类作为他的部件构建七濑，有点像车子和车轮的关系
属性(attribute): 类的一个属性，它来自于组合，而且通常是一个变量
是什么(is-a): 用来描述继承关系，如salmon is-a fish(鲑鱼是一种鱼)
有什么(has-a): 用来描述某个东西是由另外的一些东西组成的，或者某个东西有某个特征，如salmon has-a mouth(鲑鱼有一张嘴）




class x(y): 创建一个叫x的类，它是Y的一种。
class x(object): def __init__(self, j): 类x有一个__init__,它接收self和j作为参数。
class x(object): def m(self, j): 类x有一个名为m的函数，它接收self和j作为参数。
foo = x(): 将foo设为类x的一个实例
foo.m(j): 从foo中找到m函数，并使用self和j参数调用它。
foo.k = q: 从foo中获取k属性，并将其设为q。
