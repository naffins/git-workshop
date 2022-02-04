# Cursed astrology-inspired robot script

import turtle
import math
import random

turtle.speed(10)
turtle.right(90)
turtle.penup()
turtle.forward(100)
turtle.left(90)
turtle.pendown()
turtle.circle(100,None,100)

turtle.right(90)
turtle.penup()
turtle.forward(100)
turtle.left(90)
turtle.pendown()
turtle.circle(200,None,200)

turtle.right(90)
turtle.penup()
turtle.forward(100)
turtle.left(90)
turtle.pendown()
turtle.circle(300,None,300)

turtle.left(90)
turtle.penup()
turtle.forward(300)
turtle.pendown()

for i in range(12):
    turtle.forward(325)
    turtle.right(180)
    turtle.forward(325)
    turtle.right(210)
    
turtle.penup()
turtle.right(15)
    
cursed_modes = ["CHAOTIC INNOCENT",
                "CHAOTIC LAWFUL",
                "CHAOTIC IGNORANT",
                "CHAOTIC GOOD",
                "CHAOTIC NEUTRAL",
                "CHAOTIC EVIL",
                "CHAOTIC STUPID",
                "CHAOTIC SMARTASS",
                "CHAOTIC CHAOTIC",
                "CHAOTIC JOLLY",
                "CHAOTIC MANIC",
                "CHAOTIC LOLFUL",
                "CHAOTIC CURSED",
                "CHAOTIC ACID",
                "CHAOTIC ALKALI",
                "CHAOTIC TOXIC",
                "CHAOTIC WHOLESOME",
                "CHAOTIC CHILL",
                "CHAOTIC PRICK",
                "CHAOTIC CHAD",
                "CHAOTIC SILLY",
                "CHAOTIC WISE",
                "CHAOTIC JUST",
                "CHAOTIC DEAD",
                "CHAOTIC WRECK",
                "CHAOTIC IMPOSTER",
                "CHAOTIC 5HEAD",
                "CHAOTIC MEME",
                "CHAOTIC JOKER",
                "CHAOTIC CANCER",
                "CHAOTIC FRIENDLY",
                "CHAOTIC MOB",
                "CHAOTIC HOSTILE",
                "CHAOTIC STRONK",
                "CHAOTIC SUPPORTER",
                "CHAOTIC GULLIBLE"]

for i in range(12):
    turtle.forward(125)
    turtle.write(cursed_modes[i],align="center",font=("Comic Sans MS",5,"normal"))
    turtle.forward(100)
    turtle.write(cursed_modes[i+12],align="center",font=("Comic Sans MS",10,"normal"))
    turtle.forward(100)
    turtle.write(cursed_modes[i+24],align="center",font=("Comic Sans MS",15,"normal"))
    turtle.right(180)
    turtle.forward(325)
    turtle.right(210)

turtle.left(15)

year = input("Input year of birth: ")
month = input("Input month of birth in integer: ")
day = input("Input day of birth: ")
hour = input("Input hour of birth as integer (0-23): ")
minute = input("Input minute: ")
year = int(year)
month = int(month)
day = int(day)
hour = int(hour)
minute = int(minute)

random.seed((year**month/day)*math.pi+math.exp(hour*day))

cumulative_angle = (random.randint(1,17)*random.randint(1,53))%360
select_layer = random.randint(1,3)
turtle.goto(100*select_layer*math.cos(cumulative_angle/360*math.pi),
            100*select_layer*math.sin(cumulative_angle/360*math.pi))
turtle.dot(5,"black")
turtle.color("red")
turtle.pendown()
for i in range(12):
    turtle.pensize(1+1//2)
    cumulative_angle = (cumulative_angle + (random.randint(1,17)*random.randint(1,53)))%360
    select_layer = random.randint(1,3)
    turtle.goto(100*select_layer*math.cos(cumulative_angle/180*math.pi),
                100*select_layer*math.sin(cumulative_angle/180*math.pi))
turtle.dot(5,"red")
turtle.done()
print("Done. Press Ctrl+C to exit.")
while True:
    pass