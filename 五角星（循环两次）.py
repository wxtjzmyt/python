# coding=utf-8 
# 这是画一个五角星
"""
import turtle
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
"""
# 这是循环画两个五角星
"""
# import turtle

for i in range(2):
    turtle.forward(300)
    turtle.right(144)
    turtle.forward(300)
    turtle.right(144)
    turtle.forward(300)
    turtle.right(144)
    turtle.forward(300)
    turtle.right(144)
    turtle.forward(300)
    turtle.right(120)
"""

# 这是画一个五角星时用循环画
"""
import turtle
turtle.color("red","red") # 这是修改画笔颜色和修改填充颜色
turtle.begin_fill() #这是填充颜色的开始位置
for i in  range(5):
    turtle.forward(100)
    turtle.right(144)
turtle.end_fill() #这是填充颜色的结束位置
"""

# 这是画两个五角星时用循环画

import turtle
turtle.color("yellow","red") # 这是修改画笔颜色和修改填充颜色
for i in range(2):
    turtle.penup() # 这是抬起画笔
    turtle.forward(120)
    turtle.pendown() #这是放下画笔
    turtle.begin_fill() #这是填充颜色的开始位置
    for i in  range(5):
        turtle.forward(100)
        turtle.right(144)
    turtle.end_fill() #这是填充颜色的结束位置



