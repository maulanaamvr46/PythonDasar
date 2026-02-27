import turtle
import math

# ======================
# Setup layar
# ======================
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Logo SMK Prestasi Prima")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(3)

# ======================
# Lingkaran Luar (Hitam)
# ======================
t.penup()
t.goto(0, -220)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(220)
t.end_fill()

# ======================
# Ring Putih
# ======================
t.penup()
t.goto(0, -200)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(200)
t.end_fill()

# ======================
# Lingkaran Biru Tengah
# ======================
t.penup()
t.goto(0, -160)
t.pendown()
t.color("#1f2f5f")  # biru tua
t.begin_fill()
t.circle(160)
t.end_fill()

# ======================
# Fungsi teks melingkar
# ======================
def text_circle(text, radius, start_angle):
    angle = start_angle
    for char in text:
        t.penup()
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        t.goto(x, y)
        t.setheading(angle - 90)
        t.write(char, align="center", font=("Arial", 12, "bold"))
        angle -= 8

# ======================
# Teks Atas
# ======================
text_circle("SEKOLAH MENENGAH KEJURUAN", 180, 110)

# ======================
# Teks Bawah
# ======================
text_circle("PRESTASI PRIMA", 180, -70)

# ======================
# Bintang kiri
# ======================
def star(x, y, size):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color("black")
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

star(-150, 0, 20)
star(130, 0, 20)

# ======================
# Lingkaran kecil atas
# ======================
t.penup()
t.goto(0, 60)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(25)
t.end_fill()

t.penup()
t.goto(0, 70)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(15)
t.end_fill()

# ======================
# Tangan (Versi Sederhana)
# ======================
t.penup()
t.goto(-30, -80)
t.setheading(0)
t.pendown()
t.color("red")
t.begin_fill()

t.forward(60)
t.left(90)
t.forward(120)
t.left(90)
t.forward(20)
t.left(90)
t.forward(80)
t.right(90)
t.forward(20)
t.right(90)
t.forward(80)
t.left(90)
t.forward(20)
t.left(90)
t.forward(120)
t.left(90)
t.forward(60)
t.left(90)
t.forward(120)

t.end_fill()

turtle.done()