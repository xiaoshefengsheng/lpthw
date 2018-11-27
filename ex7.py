
print("mary had a little lamb.")
# 在字符串后加.format()格式化括号中的变量或字符串，与f配合{}一样
print("its fleece was white as {}.".format('snow'))
print(f"its fleece was white as {'snow'}")
print("and everywhere that mary went.")
# 如下实现的是字符串.重复了10次，即乘10
print("." * 10) # what'd that do?

end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "b"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# 字符串相加就是组合的意思。 end= ' '是在结尾增加空格，而不是默认值end=''换行。
print(end1 + end2 + end3 + end4 + end5 + end6 , end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
