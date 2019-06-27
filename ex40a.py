#定义一个类song,类里有两个函数，self.lyrics歌词。函数sing_me_a_song，当歌词在字符串中，逐行打印
class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
	
#	def __init__(self, music_list):
#		self.music_list = music_list
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)
			
	def sing_me_a_list(self):
		for line in self.lyrics:
			print(line)
#实例化类song,并把歌词列表（按','分割的是列表）参数传进去			
happy_body = Song(["Happy birthday to you",
					"I don't want to get sued",
					"so I'll stop right there"])
#实例化类song,把歌词列表参数写入					
#bulls_on_parade = Song(["They rally around the family",
#						"with pockets full of shells"])
#使用类包含的函数sing_me_a_song逐行打印歌词字符串						
happy_body.sing_me_a_song()

#bulls_on_parade.sing_me_a_song()

zhoujielun_list = Song(["千里之外",
						"双节棍",
						"青花瓷"])
zhoujielun_list.sing_me_a_song()

