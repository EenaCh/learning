from turtle import Turtle, Screen
import random
import time


class Point:
    def __init__(self, x=0, y=0, sym=''):
        self.x = x
        self.y = y
        self.sym = sym

    def Move(self, offset, direction):
        if direction == 'RIGHT':
            self.x += offset
        elif direction == 'LEFT':
            self.x -= offset
        elif direction == 'UP':
            self.y += offset
        elif direction == 'DOWN':
            self.y -= offset

    def Draw(self):
        move.goto(self.x, self.y)
        move.write(self.sym)

    def Clear(self):
        move.color('#CDFEFB')
        self.Draw()
        move.color('black')

    def IsHit(self, p):
        return p.x == self.x and p.y == self.y


class Figure:
    pList = []

    def IsHit(self, figure):
        for p in self.pList:
            if figure.IsHit(p):
                return True
        return False

    def Drow(self):
        for p in self.pList:
            p.Draw()


class HorizontalLine(Figure):
    def __init__(self, xLeft, xRight, y, sym):
        self.pList = []
        for x in range(xLeft, xRight+1, 10):
            self.pList.append(Point(x, y, sym))


class VerticalLine(Figure):
    def __init__(self, yUp, yDown, x, sym):
        self.pList = []
        for y in range(yUp, yDown+1, 10):
            self.pList.append(Point(x, y, sym))


class Snake(Figure):
    def __init__(self, tail, lenght, direction):
        self.pList = []
        self.direction = direction
        for i in range(0, lenght, 10):
            p = Point(tail.x, tail.y, tail.sym)
            p.Move(i, direction)
            self.pList.append(p)

    def Move(self):
        tail = self.pList[0]
        self.pList.remove(tail)
        head = self.GetNextPoint()
        self.pList.append(head)

        tail.Clear()
        head.Draw()

    def GetNextPoint(self):
        head = snake.pList[-1]
        nextPoint = Point(head.x, head.y, head.sym)
        nextPoint.Move(10, self.direction)
        return nextPoint

    def Eat(self, food):
        head = self.GetNextPoint()
        if head.IsHit(food):
            move.color('white')
            food.Draw()
            move.color('black')
            food.sym = head.sym
            self.pList.append(food)
            return True
        else:
            return False

    def IsHitTail(self):
        head = self.pList[-1]
        for i in range(len(self.pList) - 1):
            if head.IsHit(self.pList[i]):
                return True
        return False

    def HandleKey(self):
        screen.onkey(up, "Up")
        screen.onkey(left, "Left")
        screen.onkey(right, "Right")
        screen.onkey(down, "Down")
        screen.listen()
        self.Move()


class FoodCreator:
    def __init__(self, mapWidth, mapHight, sym):
        self.mapWidth = mapWidth
        self.mapHight = mapHight
        self.sym = sym

    def CreateFood(self):
        x = random.randrange((-1 * self.mapWidth) + 10, self.mapWidth - 10, 10)
        y = random.randrange((-1 * self.mapHight) + 10, self.mapHight - 10, 10)
        return Point(x, y, self.sym)


class Walls:
    def __init__(self, mapWidth, mapHight):
        upLine = HorizontalLine(-1 * mapWidth, mapWidth, -1 * mapHight, '+')
        downLine = HorizontalLine(-1 * mapWidth, mapWidth, mapHight, '+')
        leftLine = VerticalLine(-1 * mapHight, mapHight, -1 * mapWidth, '+')
        rightLine = VerticalLine(-1 * mapHight, mapHight, mapWidth, '+')
        self.wallList = [upLine, downLine, leftLine, rightLine]

    def IsHit(self, figure):
        for wall in self.wallList:
            if wall.IsHit(figure):
                return True
        return False

    def Draw(self):
        for wall in self.wallList:
            wall.Drow()


def up():
    global snake
    snake.direction = 'UP'
    time.sleep(0.2)
    snake.Move()


def down():
    global snake
    snake.direction = 'DOWN'
    time.sleep(0.2)
    snake.Move()


def left():
    global snake
    snake.direction = 'LEFT'
    time.sleep(0.2)
    snake.Move()


def right():
    global snake
    snake.direction = 'RIGHT'
    time.sleep(0.2)
    snake.Move()


screen = Screen()
screen.setup(800, 350)
screen.title("Snake")
screen.bgcolor("#CDFEFB")
move = Turtle()
move.hideturtle()
move.up()

# Отрисовка рамки
walls = Walls(360, 120)
walls.Draw()

p = Point(-320, 70, '*')
snake = Snake(p, 40, 'RIGHT')
snake.Drow()

foodCreator = FoodCreator(360, 120, '$')
food = foodCreator.CreateFood()
food.Draw()

while True:
    if walls.IsHit(snake) or snake.IsHitTail():
        break
    if snake.Eat(food):
        food = foodCreator.CreateFood()
        food.Draw()
    snake.HandleKey()

screen.exitonclick()
