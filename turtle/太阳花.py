# coding=utf-8  
import turtle  
  
# 同时设置pencolor=color1, fillcolor=color2  
turtle.color("red", "yellow")  
turtle.speed(10)
turtle.begin_fill()  
for i in range(50):  
    turtle.forward(200)  
    turtle.left(170)  
turtle.end_fill()
turtle.mainloop()

