shengs = {'山西' : '晋','陕西' : '陕','河北' :'冀','北京' : '京', '山东' : '鲁'}
shis = {'陕' : '西安','鲁' : '青岛' ,'冀' : '石家庄', '京' : '北京市'}

print('-' * 10)
print(shengs)
print(shis)

#添加一些城市字典
print('-' * 10)
shis['晋'] = '太原'
shis['豫'] = '郑州'

#打印部分shi的信息值
print('-' * 10)
print(shis['晋'])
print(shis['豫'])

#打印部分省简称
print('-' * 10)
print("山西省的简称是: ",shengs['山西'])
print("河北省的简称是：",shengs['河北'])

#用省简称去匹配城市名
print('-' * 10)
print("属于陕西省有的城市是：",shis[shengs['陕西']])
print("属于河北省的城市是：",shis[shengs['河北']])

#格式化打印每一个省及其简称
print('-' * 10)
for sheng , sheng_jiancheng in list(shengs.items()):
    print(f"{sheng} 的简称是： {sheng_jiancheng}")
print(list(shengs.items()))

#格式化打印 省简称与城市
print('-' * 10)
for sheng_jiancheng , shi in list(shis.items()):
    print(f"{sheng_jiancheng} 下有城市：{shi}")
print(list(shis.items()))

#打印所有关联信息
print('-' * 10)
for sheng , sheng_jiancheng in list(shengs.items()):
    print(f"{sheng} 的简称是： {sheng_jiancheng}")
    print(f"并且有城市: {shis[sheng_jiancheng]}")
	
#尝试查找不存在的省份
print('-' * 10)
sheng = shengs.get('湖南')

if not sheng:
    print("抱歉，找不到湖南省名称")
#尝试查找不存在的城市，并返回默认值	
print('-' * 10)
shi = shis.get('上海','这个不存在')
print(f"在shis字典中查找'上海'城市：{shi}")

#根据输入的阿拉伯数字转换为大写数字
dict = {0:'零',1:'一',2:'二',3:'三',4:'四',5:'五',6:'六',7:'七',8:'八',9:'九'}
number = input('>>>:')
print("".join([dict[int(key)] for key in number]))


dict = {'0':'零','1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九'}
number = input('>:')
for i in number:
	print(dict[i],end='')
# print('\n')
# print('-' * 10)

num = {'0':'零','1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九'}
money_num = {'0':'零','1':'壹','2':'贰','3':'叁','4':'肆','5':'伍','6':'陆','7':'柒','8':'捌','9':'玖'}
number = input('>:')
print("数字大写是:")
for i in number:
	print(num[i],end='')
print('\n')
print('-' * 10)
print("\n货币大写是:")
for i in number:
	print(money_num[i],end='')