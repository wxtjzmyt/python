# 练习数据类型

#字符串类型，可以用单引号，也可以用双引号
e = 'I am a student!'
print(e)
e1 = "I am a student!"
print(e)
#使用\做转义字符
f = 'I\'m a student!'
print(f)
f1 = "I'm a student!"
print(f1)
g = 'Tom say:"I am a student!"'
print(g)
g1 = "Tom say:\"I'm a student!\""
print(g1)


# 数字类型
a = 3
'''
字符串拼接，必须用str将变量先转换成字符串；
字符串拼接的方式，打印出来时，连接处没有空格；
用print打印多个变量时，连接处有空格。
'''
a1 = 'a = '+str(a)+',a的数据类型是'+str(type(a))
print('a = ',str(a),'a的数据类型是',type(a))
print(a1)
b = 2.5
print(type(b))
c = 2+3j
print(type(c))
d = a + c
print(type(d))
