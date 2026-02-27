import turtle

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("skyblue")
screen.title("Gambar Pemandangan")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# ======================
# Fungsi gambar gunung
# ======================
def gunung(x, y, ukuran):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("darkgreen")
    t.begin_fill()
    t.goto(x + ukuran, y + ukuran)
    t.goto(x + ukuran*2, y)
    t.goto(x, y)
    t.end_fill()

# ======================
# Fungsi gambar rumah
# ======================
def rumah(x, y):
    # Badan rumah
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    for _ in range(2):
        t.forward(120)
        t.left(90)
        t.forward(80)
        t.left(90)
    t.end_fill()

    # Atap
    t.goto(x, y+80)
    t.color("red")
    t.begin_fill()
    t.goto(x+60, y+140)
    t.goto(x+120, y+80)
    t.goto(x, y+80)
    t.end_fill()

# ======================
# Matahari
# ======================
t.penup()
t.goto(250, 200)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()

# ======================
# Rumput
# ======================
t.penup()
t.goto(-400, -50)
t.pendown()
t.color("green")
t.begin_fill()
for _ in range(2):
    t.forward(800)
    t.right(90)
    t.forward(200)
    t.right(90)
t.end_fill()

# ======================
# Gunung
# ======================
gunung(-300, -50, 200)
gunung(-50, -50, 250)
gunung(200, -50, 180)

# ======================
# Jalan
# ======================
t.penup()
t.goto(-100, -50)
t.pendown()
t.color("gray")
t.begin_fill()
t.goto(100, -50)
t.goto(50, -250)
t.goto(-50, -250)
t.goto(-100, -50)
t.end_fill()

# ======================
# Rumah
# ======================
rumah(-60, -50)

turtle.done()