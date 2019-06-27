#create a mapping of state to abbreviation 创建州对应的简称字典
states = {
    'oregon': 'or',
    'florida': 'fl',
    'california': 'ca',
    'new york': 'ny',
    'michigan': 'mi'
}

#create a basic set of states and some cities in them  创建州简称对应城市字典
cities = {
    'ca': 'san francisco',
    'mi': 'detroit',
    'fl': 'jacksonville'
}

#add some more cities 添加州简称对应城市到cities字典
cities['ny'] = 'new york'
cities['or'] = 'portland'

#print out some cities  打印部分州简称对应城市字典信息
print('-' * 10)  #打印-分割线
print("ny state has: ", cities['ny'])    #ny 州有new york城市
print("or state has: ", cities['or'])    

#print some states  打印部分州简称字典信息
print('-' * 10)
print("michigan's abbreviation is: ", states['michigan'])  #michigan的简称是mi
print("florida's abbreviation is: ", states['florida'])

# do it by using the state then cities dict  使用州简称字典查州对应城市字典中的城市名
print('-' * 10)
print("michigan has: ", cities[states['michigan']])  #michigan简称mi，再用cities查找mi对应城市
print("florida has: ", cities[states['florida']])

#print every state abbreviation  打印所有州简称
print('-' * 10)
for state, abbrev in list(states.items()):      #当 州名，简称 在list(states.items()
    print(f"{state} is abbreviated  {abbrev}")  #打印格式化字符串，大括号内输出变量值

#print every city in state  格式化打印所有州简称对应城市信息
print('-' * 10)
for abbrev, city in list(cities.items()):   #当简称、城市名在list(cities.items())
    print(f"{abbrev} has the city {city}")  #格式化输出简称和城市 

#now do both at the same time 输出所有对应信息
print('-' * 10)
for state, abbrev in list(states.items()):  #通过州名和简称
    print(f"{state} state is abbreviated {abbrev}")  #输出州名和简称
    print(f"and has city {cities[abbrev]}")  #输出简称对应的城市
	
print('-' * 10)
#safely get a abbreviation by state that might not be there
state = states.get('texas')   #使用get方法查找state键值为texas的简称

if not state:  #如果没有state对应的值
    print("sorry ,no texas.")   #输出无该州名

#get a city with a default values   get方法设置查找州名对应的城市，不存在则返回一个默认值
city = cities.get('tx', 'does not exist')   #键值为tx，如果不存在则返回 :does not exist
print(f"the city for the state 'tx' is :{city}")