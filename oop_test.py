import random
from urllib.request import urlopen
import sys
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []
#定义一个字典PHRASES，键值中都有特殊符号% @ *等。
PHRASES = {
	"class %%%(%%%):":
	"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)":
	"class %%% has-a __init__ thar takes self and *** params.",
	"class %%%(object):\n\tdef ***(self, @@@)":
	"class %%% has-a function *** that takes self and @@@ parames.",
	"*** = %%%()":
	"Set *** to an instance of class %%%.",
	"***.***(@@@)":
	"From *** get the *** function, call it with params self, @@@.",
	"***.*** = '***'":
	"From *** get the *** attribute and set it to '***'."
}
#do they want to drill phrases first 是否先练习短语
#如果执行代码时有2个参数，且第2个参数为english，则赋值PHRASE_FIRST为True
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False
print(PHRASE_FIRST)	
#load up the words from the website 从网站下载单词
#当word在urlopen(WORD_URL).readlines()逐行读取时，去除单词头尾空白并转为字符串，追加到列表WORDS
for word in urlopen(WORD_URL).readlines():
	WORDS.append(str(word.strip(),encoding="utf-8"))
#print(WORDS)  #调试用输出
#定义函数convert，两个参数	
def convert(snippet,phrase):
#class_names赋值为列表:统计字符串"%%%"在snippet中出现的次数,根据次数，随机抽样WORDS列表。并将抽样进行首字母大写，其余全小写处理
	class_names = [w.capitalize() for w in
					random.sample(WORDS, snippet.count("%%%"))]
#other_names赋值为列表:统计snippet中出现"***"字符串的次数，并根据几次随机抽样WORDS
	other_names = random.sample(WORDS, snippet.count("***"))
#定义两个空列表results、param_names
	results = []
	param_names = []
#统计snippet中出现"@@@"字符串的次数，当i在这个区间，param_count赋值为随机值1/2/3，随机取样，并添加,到取样。结果赋值给列表param_names
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(
			random.sample(WORDS, param_count)))
#当sentence在参数中，result复制列表sentence[:]
	for sentence in snippet, phrase:
		result = sentence[:]
		
		#fake class names 仿造类名，当word在列表class_names，则把"%%%"字符串替换为word,只替换一次
		for word in class_names:
			result = result.replace("%%%", word, 1)
			
		#fake other names 仿造其他名，当word在列表other_names，则把"***"字符串替换为word,只替换一次
		for word in other_names:
			result = result.replace("***", word, 1)
		
		#fake parameter lists 仿造参数列表，当word在列表param_names，则把"@@@"字符串替换为word,只替换一次
		for word in param_names:
			result = result.replace("@@@", word, 1)
		#执行追加，将result追加到results列表	
		results.append(result)
	#返回results值	
	return results
	
#keep going until they hit CTRL-D 保持执行，直到按ctrl-d停止
#try语句，尝试执行代码，出错后到except
try:
	while True:
		snippets = list(PHRASES.keys())  #将字典PHRASES的键作为列表
		print("输出snippets看下 > ",snippets)  #调试查看snippets，为字典的键
		random.shuffle(snippets)    #随机排序列表元素
		print("再输出一次snippets看下 > ",snippets)  #调试查看snippets，已处理为随机显示
		for snippet in snippets:
			phrase = PHRASES[snippet]    #获取字典的value
			question, answer = convert(snippet, phrase)  #question,answer赋值为函数convert处理两个参数
			print("这是第一次convert后：",question, answer)
			if PHRASE_FIRST:    #如果为真，则前后调换值
				question, answer = answer, question
			print("这是第二次做了if判断后，前后调换：",question, answer)	
			print("这是单独打印question",question)
			
			input("> ")
			print(f"单独打印ANSWER: {answer}\n\n")
except EOFError:
	print("\nBye")