import turtle
from random import choice, randint

# ЗАРАЗ МИ РОБИМО ПОЛЕ І ВІКНО ГРИ
window = turtle.Screen()
window.title("Ping-Pong")  # НАЗВА ВІКНА
window.setup(width=1.0, height=1.0)  # ВІКНО РОЗТЯГНЕТЬСЯ НА ВЕСЬ ЕКРАН
window.bgcolor("black")
window.tracer(2)

border = turtle.Turtle()  # ПРИСВОЮЄМО ЧЕРЕПАШКУ
border.speed(0)  # ЗАДАЄМО ШВИДКІСТЬ ЩОБ МАЛЮВАЛО ШВИДШЕ
border.color('green')  # РОБИМО ЗАДНІЙ ФОН ЗЕЛЕНИМ
border.begin_fill()
border.goto(-500, 300)  # ПЕРЕНОСИМОСЬ НА КООРДИНАТИ
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()

border.goto(0, 300)
border.color('white')
border.setheading(270)  # ПЕРЕДАЄ В ЯКУ СТОРОНУ БУДЕ ДИВИТИСЬ ЧЕРЕПАШКА(270 ВНИЗ)
for i in range(25):
    if i % 2 == 0:
        border.forward(24)  # МАЛЮЄМО ВІДРІЗОК ДОВЖИНОЮ 24
    else:
        border.up()  # ПІДНІМАЄМО МАРКЕР
        border.forward(24)
        border.down()  # ВПУСКАЄМО МАРКЕР
border.hideturtle()  # ЗАБИРАЄМО СТРІЛОЧКУ

rocket_a = turtle.Turtle()
rocket_a.speed(0)
rocket_a.color('white')  # ПРИСВОЮЄМО КОЛІР ПЕРШОЇ РАКЕТКИ
rocket_a.shape('square')  # ПРИСВОЮЄМОМ ФУРМУ ПЕРШОЇ РАКЕТКИ
rocket_a.shapesize(stretch_len=1, stretch_wid=5)  # РОЗМІР РАКЕТКИ
rocket_a.penup()  # РАКЕТКА ЗА СОБОЮ НЕ ЛИШАЄ СЛІДІВ
rocket_a.goto(-450, 0)

rocket_b = turtle.Turtle()
rocket_b.speed(0)  # ПРИСВОЮЄМО ШВИДКІСТЬ
rocket_b.shape("square")  # ФОРМУ
rocket_b.color("white")  # КОЛІР
rocket_b.shapesize(stretch_wid=5, stretch_len=1)  # РОЗМІР
rocket_b.penup()  # РОБИМ ЩОБ НЕ ЛИШАВ ЗА СОБОЮ СЛІДІВ
rocket_b.goto(450, 0)

FONT = ('Arial', 44)
score_a = 0
s1 = turtle.Turtle(visible=False)
s1.penup()
s1.color('white')
s1.setposition(-200, 300)
s1.write(score_a, font=FONT)
score_b = 0
s2 = turtle.Turtle(visible=False)
s2.penup()
s2.color('white')
s2.setposition(200, 300)
s2.write(score_a, font=FONT)

def move_up():
    y = rocket_a.ycor() + 10  # ДІЗНАЄМОСЬ ПОЛОЖЕННЯ РАКЕТКИ
    if y > 250:
        y = 250
    rocket_a.sety(y)


def move_down():
    y = rocket_a.ycor() - 10
    if y < -250:
        y = -250
    rocket_a.sety(y)


def move_up_b():
    y = rocket_b.ycor() + 10
    if y > 250:
        y = 250
    rocket_b.sety(y)


def move_down_b():
    y = rocket_b.ycor() - 10
    if y < -250:
        y = -250
    rocket_b.sety(y)


ball = turtle.Turtle()
ball.shape('circle')
ball.speed(0)
ball.color('red')
ball.dx = -3  # ШВИДКІСТЬ МЯЧИКА
ball.dy = -3
ball.penup()

window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_up_b, "i")
window.onkeypress(move_down_b, "k")

while True:
    assert isinstance(window, object)
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:
        ball.dy = -ball.dy

    if ball.ycor() <= -290:
        ball.dy = -ball.dy

    if ball.xcor() >= 490:
        score_b += 1
        s2.clear()
        s2.write(score_b, font=FONT)
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])  # ВИВОДИМ ПОЧАТКОВУ ПОЗИЦІЮ ЛЮБУ З ЦИХ ЧИСЕЛ
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

    if ball.xcor() <= -490:
        score_a += 1
        s1.clear()
        s1.write(score_a,font=FONT)
        ball.goto(0, randint(-150, 150))  # ВИВОДИТЬ МЯЧ НА ПОЧАТКУ У РАНДОМНОМУ ПОЛОЖЕНІ ВІД -150 ДО 150
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

    if ball.ycor() >= rocket_b.ycor() - 50:
        if ball.ycor() <= rocket_b.ycor() + 50:
            if ball.xcor() >= rocket_b.xcor() - 5:
                if ball.xcor() <= rocket_b.xcor() + 5:
                    ball.dx = -ball.dx

    if ball.xcor() >= rocket_a.xcor() - 50:
        if ball.xcor() <= rocket_a.xcor() + 50:
            if ball.ycor() >= rocket_a.ycor() - 5:
                if ball.ycor() <= rocket_a.ycor() + 5:
                    ball.dx = -ball.dx

window.mainloop()
