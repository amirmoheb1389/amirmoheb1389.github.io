#start
import turtle
import winsound
import sys 
#backend
def map(x,y,name):
    return name.goto(x,y)
def penup(name):
    return name.penup()
def pendown(name):
    return name.pendown()
def goright(num,name):
    return name.right(num)
def goleft(name,num):
    return name.left(num)
def move(name,num):
    return name.forward(num)
def coor_x(name):
    return name.xcor()
def coor_y(name):
    return name.ycor()
def keypress(key,command,name):
    return name.onkeypress(command,key)
def speed(name,num):
    return name.speed(num)
def dir(name):
    return name.heading()
def set_dir(name,num):
    return name.setheading(num)
def list():
    return turtle.listen()
def sound_bb(hertz,sec):
    return winsound.Beep(hertz,(sec / 1000))
def sound_de():
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
def sound_file(file):
    winsound.PlaySound((file+".wav"), winsound.SND_FILENAME)
def click(name,funk):
    return name.onclick(funk)
def write(name, text):
    with open((name+".pyf"),"a") as f:
        f.write(text)
        f.close()
def closed(name):
    with open((name+".pyf"),"r") as f:
        return f.read()
#frontend
turtle.title("pyforge")
def back_color(color,name):
    return name.bgcolor(color)
def back_image(name,image):
    return name.bgpic(image)
def title(name,title):
    return name.title(title)
def window():
    return turtle.Screen()
def window_size(name,x , y):
    return name.setup(x, y)
def car():
    return turtle.Turtle() 
def car_color(name, color): 
    return name.color(color)
def car_shape(name, met, shape):
    if met == "shape":
        return name.shape(shape)
    elif met == "image":
        return name.shape(shape)
def car_size(w, l, name):
    return name.turtlesize(stretch_wid=w, stretch_len=l)
def car_pen_setting(color, size, name):
    return name.pencolor(color),name.pensize(size)
def text(text,font,location,name):
    return name.write(text,font,location)
def shape(name,r,amount,side):
    return name.circle(r,(amount * 360),side)
def car_ramove(name):
    return name.hideturtle()
#end
def completed():
    return turtle.done()
def exit():
    return sys.exit()
