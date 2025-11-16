#   Add your code here and add comments to your code 
#   to describe what each section of code is doing
screen_h = 400
screen_w = 600
startx = 0
starty = 0
turtle_scale = 1


import turtle as trtl
t = trtl.Turtle()
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
wn.bgpic("greytable.png")

#making store sign
def rectangle():
  t.penup()
  t.goto(-150,200)
  t.pendown()
  t.fillcolor("firebrick")
  t.begin_fill()
  t.goto(150,200)
  t.right(90)
  t.goto(150,100)
  t.right(90)
  t.goto(-150,100)
  t.right(90)
  t.goto(-150,200)
  t.end_fill()
  t.penup()
  
def words():
  #B
  t.goto(-140,180)
  t.pendown()
  t.pencolor("white")
  t.pensize(10)
  t.right(180)
  t.goto(-140,120)
  t.goto(-140,150)
  t.right(270)
  t.circle(15,180)
  t.goto(-140,120)
  t.right(180)
  t.circle(15,180)
  #U
  t.penup()
  t.goto(-110,180)
  t.pendown()
  t.goto(-110,135)
  t.right(270)
  t.circle(17,180)
  t.goto(-76,180)
  #R
  t.penup()
  t.goto(-60,180)
  t.pendown()
  t.goto(-60,120)
  t.goto(-60,150)
  t.right(90)
  t.circle(15,180)
  t.goto(-60,150)
  t.goto(-40,120)
  #g
  t.penup()
  t.goto(0,180)
  t.pendown()
  t.circle(30,180)
  t.goto(0,150)
  t.goto(-12,150)
  #E
  t.penup()
  t.goto(20,180)
  t.pendown()
  t.goto(20,120)
  t.goto(35,120)
  t.penup()
  t.goto(35,150)
  t.pendown()
  t.goto(20,150)
  t.goto(20,180)
  t.goto(35,180)
  #R
  t.penup()
  t.goto(55,180)
  t.pendown()
  t.goto(55,120)
  t.goto(55,150)
  t.circle(15,180)
  t.goto(55,150)
  t.goto(75,120)
  #S
  t.penup()
  t.goto(120,180)
  t.pendown()
  t.goto(90,180)
  t.goto(90,150)
  t.goto(120,150)
  t.goto(120,120)
  t.goto(90,120)
  
rectangle()
words() 

#printing options and welcome
print("Welcome to Build a Burger!") 
print("We have many options for inside your personalized burger:")
print("1. cheese + meat")
print("2. lettuce")
print("3. tomatoes")
print("4. avocados")
print("5. onions")

#making bottom bun
def bottom_bun():
  t.penup()
  t.pensize(8)
  t.goto(-80,-150)
  t.pendown()
  t.pencolor("sandy brown")
  t.fillcolor("sandy brown")
  t.begin_fill()
  t.goto(80,-150)
  t.goto(90,-130)
  t.goto(-90,-130)
  t.goto(-80,-150)
  t.end_fill()
  t.penup()
  t.goto(-90,-130)
  t.right(180)
  t.goto(-80,-130)
  t.right(270)  
bottom_bun()
def top_bun():
  t.penup()
  t.pencolor("sandy brown")
  t.fillcolor("sandy brown")
  t.forward(10)
  t.right(90)
  t.begin_fill()
  t.forward(170)
  t.right(245)
  t.pendown()
  t.circle(100,130)
  t.right(245)
  t.forward(180)
  t.end_fill()

#other options
def meatandcheese():
  t.forward(5)
  t.pensize(8)
  t.right(90)
  t.pendown()
  t.fillcolor("saddle brown")
  t.pencolor("saddle brown")
  t.begin_fill()
  t.forward(160)
  t.right(270)
  t.forward(18)
  t.right(270)
  t.forward(160)
  t.right(270)
  t.forward(18)
  t.end_fill()
  t.right(180)
  t.forward(19)
  t.right(90)
  t.pencolor("orange")
  for i in range(8):
    t.right(90)
    t.forward(8)
    t.right(180)
    t.forward(8)
    t.right(90)
    t.forward(20)
  t.penup()
  t.right(180)
  t.forward(160)
  t.right(90)
def lettuce():
  t.penup()
  t.pensize(8)
  t.forward(20)
  t.pencolor("lawn green")
  t.right(90)
  t.fillcolor("lawngreen")
  t.begin_fill()
  t.forward(160)
  t.right(90)
  t.forward(13)
  t.right(90)
  t.forward(160)
  t.right(90)
  t.forward(13)
  t.end_fill()
def tomatoes():
  t.penup()
  t.pensize(8)
  t.forward(5)
  t.right(90)
  t.pendown()
  t.pencolor("red")
  t.fillcolor("red")
  t.begin_fill()
  t.forward(160)
  t.right(270)
  t.forward(5)
  t.right(270)
  t.forward(160)
  t.right(270)
  t.forward(5)
  t.end_fill()
  t.right(180)
  t.forward(5)
  t.penup()
def avocados(): 
  t.penup()
  t.pensize(8)
  t.forward(5)
  t.right(90)
  t.pencolor("olive drab")
  t.fillcolor("olive drab")
  t.begin_fill()
  t.forward(160)
  t.right(270)
  t.forward(8)
  t.right(270)
  t.forward(160)
  t.right(270)
  t.forward(8)
  t.end_fill()
  t.penup()
  t.right(180)
  t.forward(8)
def onions():
  t.penup()
  t.forward(5)
  t.right(90)
  t.pendown()
  t.pensize(4)
  t.pencolor("pale violet red")
  t.fillcolor("floral white")
  t.begin_fill()
  t.forward(160)
  t.right(270)
  t.forward(8)
  t.right(270)
  t.forward(160)
  t.right(270)
  t.forward(8)
  t.right(180)
  t.forward(8)
  t.end_fill()
  t.penup()


print("What would you like on the first layer of your burger?")
layer1 = int(input("Enter the number of your choice, or say 0 if you don't want any more"))

if layer1 == int(0):
  top_bun()
  print("Your burger is finished, have a good day!")
else:
  if layer1 == int(1):
    meatandcheese()
  if layer1 == int(2):
    lettuce()
  if layer1 == int(3):
    tomatoes()
  if layer1 == int(4):
    avocados()
  if layer1 == int(5):
    onions()
  layer2 = int(input("2nd layer?"))
  if layer2 == int(0):
    top_bun()
    print("Your burger is finished, have a good day!")
  else:
    if layer2 == int(1):
      meatandcheese()
    if layer2 == int(2):
      lettuce()
    if layer2 == int(3):
      tomatoes()
    if layer2 == int(4):
      avocados()
    if layer2 == int(5):
      onions()
    layer3 = int(input("3rd layer?"))
    if layer3 == int(0):
      top_bun()
      print("Your burger is finished, have a good day!")
    else:
      if layer3 == int(1):
        meatandcheese()
      if layer3 == int(2):
        lettuce()
      if layer3 == int(3):
        tomatoes()
      if layer3 == int(4):
        avocados()
      if layer3 == int(5):
        onions()
      layer4 = int(input("4th layer?"))
      if layer4 == int(0):
        top_bun()
        print("Your burger is finished, have a good day!")
      else:
        if layer4 == int(1):
          meatandcheese()
        if layer4 == int(2):
          lettuce()
        if layer4 == int(3):
          tomatoes()
        if layer4 == int(4):
          avocados()
        if layer4 == int(5):
          onions()
        layer5 = int(input("5th layer?"))
        if layer5 == int(0):
          top_bun()
          print("Your burger is finished, have a good day!")
        else:  
          if layer5 == int(1):
            meatandcheese()
          if layer5 == int(2):
            lettuce()
          if layer5 == int(3):
            tomatoes()
          if layer5 == int(4):
            avocados()
          if layer5 == int(5):
            onions()
          top_bun()
          print("Your burger is finished, have a great day!")
        


  
wn = trtl.Screen()
wn.mainloop()
