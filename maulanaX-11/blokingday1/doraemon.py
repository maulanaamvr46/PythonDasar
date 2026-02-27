import turtle

# Setup layar
screen = turtle.Screen()
screen.bgcolor("white")

dora = turtle.Turtle()
dora.speed(0)

# Kepala (biru)
dora.penup()
dora.goto(0, -100)
dora.pendown()
dora.color("blue")
dora.begin_fill()
dora.circle(150)
dora.end_fill()

# Wajah (putih)
dora.penup()
dora.goto(0, -70)
dora.pendown()
dora.color("white")
dora.begin_fill()
dora.circle(120)
dora.end_fill()

# Mata kiri
dora.penup()
dora.goto(-35, 80)
dora.pendown()
dora.color("white")
dora.begin_fill()
dora.circle(30)
dora.end_fill()

# Mata kanan
dora.penup()
dora.goto(35, 80)
dora.pendown()
dora.begin_fill()
dora.circle(30)
dora.end_fill()

# Pupil kiri
dora.penup()
dora.goto(-25, 95)
dora.pendown()
dora.color("black")
dora.begin_fill()
dora.circle(10)
dora.end_fill()

# Pupil kanan
dora.penup()
dora.goto(45, 95)
dora.pendown()
dora.begin_fill()
dora.circle(10)
dora.end_fill()

# Hidung
dora.penup()
dora.goto(0, 50)
dora.pendown()
dora.color("red")
dora.begin_fill()
dora.circle(15)
dora.end_fill()

# Garis tengah wajah
dora.penup()
dora.goto(0, 50)
dora.setheading(-90)
dora.pendown()
dora.forward(70)

# Mulut
dora.penup()
dora.goto(-60, 20)
dora.setheading(-60)
dora.pendown()
dora.circle(70, 120)

# Kumis kiri
dora.penup()
dora.goto(-60, 40)
dora.setheading(180)
dora.pendown()
dora.forward(60)

dora.penup()
dora.goto(-60, 20)
dora.setheading(180)
dora.pendown()
dora.forward(60)

dora.penup()
dora.goto(-60, 0)
dora.setheading(180)
dora.pendown()
dora.forward(60)

# Kumis kanan
dora.penup()
dora.goto(60, 40)
dora.setheading(0)
dora.pendown()
dora.forward(60)

dora.penup()
dora.goto(60, 20)
dora.setheading(0)
dora.pendown()
dora.forward(60)

dora.penup()
dora.goto(60, 0)
dora.setheading(0)
dora.pendown()
dora.forward(60)

dora.hideturtle()
turtle.done()