#this goes in mystuff.py
# def apple():
	# print("I AM APPLE!")
	
#this is just a variable
#tangerine = "Living reflection of a dream"

class Mystuff(object):
	
	def __init__(self):
		self.tangerine = "And now a thousand years between"
		
	def apple(self):
		print("I AM APPLE!")
		
thing = Mystuff()
thing.apple()
print(thing.tangerine)