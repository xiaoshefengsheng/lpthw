# 变量赋值为一个字符串，\t是制表符的意思，即缩进一个tab制表符。\n是换行的意思,\\转义为反斜杠\,还有如\a,\v等转义ascii码\"转义双引号等
tabby_cat = "\ti'm tabbed in."
persian_cat = "i'm split\non a line."
backslash_cat = "i'm \\ a \\ cat."

fat_cat = """
i'll do a list:
\t* cat food
\t* fishies
\t* catnip\n\t* grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
