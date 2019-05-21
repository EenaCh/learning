import turtle
import random
import math

import mr_Robot


PHI = 360 / 7
R = 50


def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def draw_pistol(base_x, base_y):
    # основной круг
    gotoxy(base_x, base_y)
    turtle.circle(80)
    # мушка
    gotoxy(base_x, base_y + 160)
    draw_circle(5, 'red')

    # барабан
    for i in range(7):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(math.sin(phi_rad) * R + base_x, math.cos(phi_rad) * R + base_y + 60)
        draw_circle(22, 'white')


def rotate_pistol(base_x, base_y, start):
    for i in range(start, random.randrange(7, 50)):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(math.sin(phi_rad) * R + base_x, math.cos(phi_rad) * R + base_y + 60)
        draw_circle(22, 'brown')
        draw_circle(22, 'white')

    gotoxy(math.sin(phi_rad) * R + base_x, math.cos(phi_rad) * R + base_y + 60)
    draw_circle(22, 'brown')
    return i % 7


turtle.speed(0)
draw_pistol(100, 100)

answer = ''
start = 0
while answer != 'N':
    answer = turtle.textinput('Играем?', 'Y/N')

    if answer == 'Y':
        start = rotate_pistol(100, 100, start)

        if start == 0:
            gotoxy(-150, 250)
            turtle.write('Вы проиграли!', font=('Arial', 18, 'normal'))
            z = random.randrange(0, 3)
            if z == 0:
                mr_Robot.duble_files('test')
            elif z == 1:
                mr_Robot.random_delete('test')
            else:
                gotoxy(-100, -50)
                turtle.write('Вам везет!', font=('Arial', 20, 'normal'))
