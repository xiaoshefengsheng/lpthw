def mima():
	pakaword = 888888
	passwd_max = 3
	error_passwd = 0
	for error_passwd in range(passwd_max):
		NewPassword = int(input("请输入密码： "))
		if NewPassword == pakaword:
			quqian()
		else:
			print("密码错误，请重新输入！")
			error_passwd += 1
			print("密码错误 %s 次" % error_passwd)
	print("密码错误三次，请取卡！")
	exit()
def quqian():
	amount = int(input("请输入金额： "))
	if amount in range(1000)[::100]:
		print(f"您成功取钱 {amount}")
		print("交易完成，请取卡！")
		exit()
	else:
		print("请输入100的倍数，且最大单次取款不超过1000元")
		quqian()

mima()
