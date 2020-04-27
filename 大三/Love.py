import turtle
import time


# 画爱心
def LittleHeart():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)


# 输入表白的语句
love = input('Please enter a love:')
# 输入署名，没有不执行
me = input('Please enter pen name:')
if love == '':
    love = 'I love you'
# 窗口大小
turtle.setup(width=900, height=500)
# 颜色
turtle.color('red', 'pink')
# 笔大小
turtle.pensize(3)
# 速度
turtle.speed(1)
# 提笔
turtle.up()
# 隐藏笔
turtle.hideturtle()
# 去到的坐标，窗口中心为0,0
turtle.goto(0, -180)
turtle.showturtle()
# 画主线
turtle.down()
turtle.speed(1)
turtle.begin_fill()
turtle.left(140)
turtle.forward(224)
# 调用画爱心
LittleHeart()
turtle.left(120)
LittleHeart()
# 画下线
turtle.forward(224)
turtle.end_fill()
turtle.pensize(5)
turtle.up()
turtle.hideturtle()
# 在心中写字
turtle.goto(0, 0)
turtle.showturtle()
turtle.color('#CD5C5C', 'pink')
# 在心中写字，font可以设置字体，align开始位置
turtle.write(love, font=('gungsuh', 30,), align='center')
turtle.up()
turtle.hideturtle()
time.sleep(2)
# 在心中写字 二次
turtle.goto(0, 0)
turtle.showturtle()
turtle.color('red', 'pink')
turtle.write(love, font=('gungsuh', 30,), align='center')
turtle.up()
turtle.hideturtle()
# 写署名
if me != '':
    turtle.color('black', 'pink')
    time.sleep(2)
    turtle.goto(180, -180)
    turtle.showturtle()
    turtle.write(me, font=(20,), align='center', move=True)

# 点击窗口关闭
window = turtle.Screen()
window.exitonclick()
