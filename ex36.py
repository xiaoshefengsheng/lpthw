#file = open('H://study2017/python/chen.txt','w')
#file.write('chenruining.com')

def text_create(name, msg):
    text_path = 'h://study2017/python/'
    full_path = text_path + name +'.txt'
    file = open(full_path,'w')
    file.write(msg)
    file.close()
    print('done')
text_create('xiaoshe', 'woshi xiaoshe')