# 引入库或者模块argv ，这个模块支持用户在运行脚本时直接后面跟参数。
from sys import argv
# read the wyss section for how to run this
# 给下面的变量赋值用户输入的参数,必须输入对应数量的参数。
script, first, second, third = argv
# 打印argv的值，type可以看到它被赋予成一个list,repr可以看到包含的就是我们脚本后面输入的参数。 这种print是常用的调试方法，直接看到值
print(">>> argv", repr(argv))
print(type(argv))
# 根据变量名，打出对应位置的参数。此处跟shell中的$0 $1 $2 $3 一样。 
print("the script is called:", script)
print("your first variable is:", first)
print("your second variable is:", second)
print("your third variable is:", third)
