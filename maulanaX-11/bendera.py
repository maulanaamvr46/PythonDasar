import turtle

# Setup layar
screen = turtle.Screen()
screen.title("Bendera Merah Putih")
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(3)
t.hideturtle()

# Fungsi gambar persegi panjang
def persegi_panjang(warna, lebar, tinggi):
    t.color(warna)
    t.begin_fill()
    for _ in range(2):
        t.forward(lebar)
        t.right(90)
        t.forward(tinggi)
        t.right(90)
    t.end_fill()

# ======================
# Tiang bendera
# ======================
t.penup()
t.goto(-200, -150)
t.setheading(90)
t.pendown()
t.pensize(6)
t.color("black")
t.forward(300)

# ======================
# Bendera Merah Putih
# ======================
t.pensize(1)
t.penup()
t.goto(-200, 100)
t.setheading(0)
t.pendown()

# Bagian merah
persegi_panjang("red", 250, 80)

# Bagian putih
t.right(90)
t.forward(80)
t.left(90)
persegi_panjang("white", 250, 80)

turtle.done()