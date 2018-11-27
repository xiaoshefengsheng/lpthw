from sys import argv

script, filename = argv
#此处只有打开文件，没有加参数
txt = open(filename)

#filename可以输入绝对目录，也可以直接输入本脚本所在的目录下的文件名称
print(f"here's your file {filename}:")
print(txt.read())

print("type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())