from ti_python_module.ti_system import *
from turtle import *
from random import *

size = 2
snake_speed = 10
snake_distance = 1
snake_color = (0, 255, 0)
apple_color = (255, 0, 0)
bg_color = (255, 255, 255)
box_color = (0, 0, 0)

t = Turtle()
t.hideturtle()
t.speed(snake_speed)
t.pencolor(snake_color)
t.pensize(size)
t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(90)
curr_heading = (90, "up")

util_t = Turtle()
util_t.hideturtle()
util_t.pencolor(apple_color)
util_t.fillcolor(box_color)
util_t.speed(0)
util_t.penup()

eraser = Turtle()
eraser.hideturtle()
eraser.hidescale()
eraser.hidegrid()
eraser.speed(0)
eraser.pencolor(bg_color)
eraser.pensize(size)
eraser.penup()
eraser.goto(0, 0)
eraser.pendown()

apples = []
def gen_apple(n = 1):
  for _ in range(n):
    x = randint(-150, 150)
    y = randint(-100, 100)
    util_t.goto(x, y)
    util_t.dot(size)
    apples.append((x, y))

def check_apple(apples, size):
  for i in range(len(apples)):
    if apples[i][0] <= t.xcor() + size and apples[i][0] >= t.xcor() - size and apples[i][1] <= t.ycor() + size and apples[i][1] >= t.ycor() - size:
      util_t.goto(apples[i][0], apples[i][1])
      util_t.pencolor(bg_color)
      util_t.dot(size)
      util_t.pencolor(apple_color)
      return (True, i)
  return (False, None)

#def rectangle(x, y):
#  for k in range(4):
#    if k % 2 == 0:
#      util_t.forward(x)
#    else:
#      util_t.forward(y)
#    util_t.right(90)

class Tail:
  def __init__(self):
    self.re = ""
    self.key = {"up":"^", "down":"v", "left":"<", "right":">"}
    self.controls = {"^":90, "v":270, "<":180, ">":0}
    self.am = 1
    self.prev = 0
  
  def update(self, direction):
    self.re += self.key[direction]
    if self.am > self.prev:
        self.prev += 0.25
    else:
        eraser.setheading(self.controls[self.re[0]])
        eraser.forward(1)
        self.re = self.re[1:]
  
  def increase(self):
    self.am += 1
  
  def get(self):
    return (self.am, self.re)

tail = Tail()
gameover = False
score = 0
k = ""
movements = []
gen_apple()
controls = {"up":90, "down":270, "left":180, "right":0}
while k != "esc" and not gameover:
#  movements.append((t.xcor(), t.ycor()))
#  movements = movements[:-1 * (score)]
#  print(movements)
  for i in movements:
    eraser.goto(i[0], i[1])
    eraser.dot(size)
  if t.xcor() >= 159 or t.xcor() <= -159 or t.ycor() >= 106 or t.ycor() <= -106:
#    util_t.goto(-50, 50)
#    util_t.pencolor(bg_color)
#    util_t.begin_fill()
#    util_t.pendown()
#    rectangle(100, 100)
#    util_t.end_fill()
#    util_t.penup()
    util_t.goto(-40, 20)
    util_t.write("Game Over")
    util_t.goto(-40, 0)
    util_t.write("Score:")
    util_t.goto(-40, -20)
    util_t.pencolor(bg_color)
    util_t.write(str(score))
    gameover = True
#  try:
#    g = controls[k]
#  except KeyError:
#    pass
#  else:
#    if curr_heading != g + 180 and curr_heading != g - 180:
#      curr_heading = g
  if k == "up" and curr_heading[0] != controls["down"]:
    curr_heading = (controls["up"], "up")
  if k == "down" and curr_heading[0] != controls["up"]:
    curr_heading = (controls["down"], "down")
  if k == "left" and curr_heading[0] != controls["right"]:
    curr_heading = (controls["left"], "left")
  if k == "right" and curr_heading[0] != controls["left"]:
    curr_heading = (controls["right"], "right")
  tail.update(curr_heading[1])
  t.setheading(curr_heading[0])
  t.forward(snake_distance)
  c = check_apple(apples, size)
  if c[0]:
    score += 1
    tail.increase()
    apples = apples[:c[1]] + apples[c[1] + 1:]
    gen_apple()
  k = get_key()
while get_key() != "esc":
  pass