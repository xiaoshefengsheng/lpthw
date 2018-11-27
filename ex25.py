#定义函数break_word,""""""这个就是函数的帮助提示。 使用.split方法处理对象,return方法返回处理结果为使用,分割的字符串列表
def break_words(stuff):
	"""this function will break ip words for us."""
	words = stuff.split(' ')
	return words
#定义函数sort_words,sort可以对list排序，sorted可以对所有可迭代的对象排序	
def sort_words(words):
	"""sorts the words."""
	return sorted(words)
#定义函数print_first_word,用pop方法移除列表的一个元素,函数为删除第一个，打印删除的值	
def print_first_word(words):
	"""prints the first word after popping it off."""
	word = words.pop(0)
	print(word)
#定义函数print_last_word,使用pop方法删除列表最后一个元素，打印删除的元素	
def print_last_word(words):
	"""prints the last word after popping it off."""
	word = words.pop(-1)
	print(word)
#定义函数sort_sentence，调用break_words处理sentence变量赋值给words,再把分割为列表的变量words调用sort_words处理后得到从a-z方向的排序	
def sort_sentence(sentence):
	"""takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
#定义函数print_first_and_last,调用break_words处理为列表，再用print_first_word处理列表的第一个元素，用print_last_word获得最后一个元素	
def print_first_and_last(sentence):
	"""prints the first and last words if the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
#定义函数print_first_and_last_sorted,words为sort_sentence处理为排序后的列表，print_first_word处理后输出删除的第一个元素，print_last_word输出删除的最后一个元素	
def print_first_and_last_sorted(sentence):
	"""sotrs the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
#本篇代码执行后，可以对比未排序处理后的列表和排序后的列表。
#排序前删除的第一个和最后一个元素，排序后删除的第一个和最后一个元素。
#主要使用了.split分割字符串为列表，.pop删除指定位置的元素，默认为最后一个。