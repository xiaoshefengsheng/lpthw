print('the game name is "eat what"?')
eat = input("please tell me ,what do eat? Such as noodles, rice, dumplings... > ")

if eat == "noodles":
	print("Okay, but you need to choose again, chow mein or noodle soup.?")
	print("enter '1', choose chow mein.")
	print("enter '2', choose noodle soup.")

	noodles_choose = input("please enter 1 or 2. > ")
	if noodles_choose == "1":
		print("All right, let's go right. To a noodle shop. ")
	elif noodles_choose == '2':
		print("OK, Let's go to Lanzhou to pull noodles.")
	else:
		print("Without this food.")

elif eat == "rice":
	print("Let's have braised chicken rice.")

elif eat == "dumplings":
	print("我们去小恒水饺店吧.")
else:	
	print("let's Order meal.")