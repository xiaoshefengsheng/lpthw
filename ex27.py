逻辑术语
and : 与
or : 或
not : 非
!= : 不等于
== : 等于
>= : 大于等于
<= : 小于等于
True : 真
False : 假

真值表

	not		真假
not False	True
not True	False

	or 			真假
True or False	True
True or True	True
False or True	True
False or False	False

	and			真假
True and False	False
True and True	True
False and True	False
False and False False

	not or		真假
not(True or False)	False
not(True or True)	False
not(False or True)	False
not(False or False)	True

	not and		真假
not(True and False)	True
not(True and True)	False
not(False and True)	True
not(False and False) True

	!=		真假
1 != 0		True
1 != 1		False
0 != 1		True
0 != 0		False

	==		真假
1 == 0		False
1 == 1 		True
0 == 1 		False
0 == 0		True