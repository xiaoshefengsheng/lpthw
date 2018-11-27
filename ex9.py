
# 定义变量days是一个字符串。  months变量赋值字符串，但是使用\n进行了换行操作。
days = "mon tue wed the fri sat sun "
months = "\njan\nfeb\nmar\napr\nmay\njun\njul\naug"

print("here are the days: ", days)
print("here are the months: ", months)
# 三个连续的引号可以输入一整段的字符串，且随意换行。可以在每行前增加\t标识制表符tab,使得每行缩进8个空格？也有可能4个。。。
print("""
\tthere's something going on the here.
\twith the three double-quotes.
\twe'll be able to type as much as we like.
\teven 4 lines if we wang, or 5, or 6.
""")