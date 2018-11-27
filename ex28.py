True and True		True
False and True		False
1 == 1 and 2 ==1	False
"test" == "test"	True
1== 1 or 2 != 1		True
True and 1 == 1		True
False and 0 != 0	False
True or 1 == 1		True
"test" == "testing"	False
1 != 0 and 2 == 1	False
"test" != "testing"  False
"test" == 1			False
not(True and False)	True
not(1 ==1 and 0 !=1) False
not(10 == 1 or 1000 == 1000) False
not(1 != 10 or 3 == 4)	False
not("testing" == "testing" and "zen" == "cool guy")	True
1 == 1 and not("testing" == 1 or 1 == 0) True
"chunky" == "bacon" and not(3 == 4 or 3 == 3)	False
3 == 3 and not("testing" == "testing" or "python" == "fun")  False

#python比较运算符：== 等于，！= 不等于，>大于，<小于，>=大于等于，<=小于等于

#and逻辑语句，1 and 3,返回3这个值。 0 and 3,返回0。 根据两个值为真，返回第二个值。任意一个为假，直接返回False。
#or逻辑语句，包含True,则只处理为True.