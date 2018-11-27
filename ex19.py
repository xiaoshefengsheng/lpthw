#定义cheese_and_crackers，处理参数为两个cheese_count,box_of_crackers.
#print(">>> ")这个可以是debug调试的一种方法，清晰的知道函数和变量引用时的值。
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(">>> cheese_count=", cheese_count, "box_of_crackers=",boxes_of_crackers)
	print(f"you have {cheese_count} cheeses!")
	print(f"you have {boxes_of_crackers} boxes of crackers!")
	print("man that's enough for a party!")
	print("get a blanket.\n")
	print("<<< exit cheese_and_crackers")

print("we can just give the function numbers directly:")
#直接调用函数，参数值为20，30. 	
cheese_and_crackers(20, 30)



print("or, we can use variables from our script:")	
amount_of_cheese = 10
amount_of_crackers = 50
#通过变量赋值参数值为10，50. 再调用函数处理变量
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("we can even do math inside too:")
#参数可以通过计算得出值，再调用函数处理值
cheese_and_crackers(10 + 20, 5 + 6)

print("and we can combine the two. variables and math:")
#参数通过计算上面的变量值再计算得出值，再调用函数处理参数
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)