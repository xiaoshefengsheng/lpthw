
# print("new,game. input month ,output seasons")
# month = int(input("please input a number of month :>"))

# if 1 <= month <= 3:
	# print("the seasons is spring")
# elif 4 <= month <= 6:
	# print("the seasons is summer")
# elif 7<= month <= 9:
	# print("the seasons is autumn")
# elif 10 <= month <= 12:
	# print("the seasons is winter")
# else:
	# print("your input number error,please return")
	
def month_seasons():
#	print("new,game. input month ,output seasons")
	month = int(input("please input a number of month :> "))

	if 1 <= month <= 3:
		print("the seasons is spring")
	elif 4 <= month <= 6:
		print("the seasons is summer")
	elif 7<= month <= 9:
		print("the seasons is autumn")
	elif 10 <= month <= 12:
		print("the seasons is winter")
	else:
		print("your input number error,please return")
		return month_seasons()
#print("new,game. input month ,output seasons")
#month = int(input("please input a number of month :>"))
month_seasons()

# from sys import argv
# script, month = argv
# month = int(month)
# def month_seasons():
# #	print("new,game. input month ,output seasons")
# #	month = int(input("please input a number of month :>"))

	# if 1 <= month <= 3:
		# print("the seasons is spring")
	# elif 4 <= month <= 6:
		# print("the seasons is summer")
	# elif 7<= month <= 9:
		# print("the seasons is autumn")
	# elif 10 <= month <= 12:
		# print("the seasons is winter")
	# else:
		# print("your input number error,please return")
# #		return month_seasons()
# #print("new,game. input month ,output seasons")
# #month = int(input("please input a number of month :>"))
# month_seasons()

