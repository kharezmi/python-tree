import turtle
import random
from collections import deque


PEN_SIZE = 10
LEAF_LINE = '0'
LINE = '1'
LINE_LENGTH = 10
ANGLE = 20


def generate_tree(iterations):
    axiom = "0"
    for _ in range(iterations):
        new_axiom = str()
        h = 0
        for c in axiom:
            if c == '0':
                new_axiom += '1[0]0'
            elif c == '1':
                new_axiom += '21'
            elif c == '2':
                if h > 2 and random.random() > 0.9:
                    new_axiom += '3[0]3'
                else:
                    new_axiom += '2'
            elif c == '[':
                h += 1
                new_axiom += c
            elif c == ']':
                h -= 1
                new_axiom += c
            else:
                new_axiom += c

        axiom = new_axiom

    return '1'*5 + axiom


def main():
    global PEN_SIZE
    axiom = generate_tree(12)
    turtle.tracer(0)
    turtle.speed(0)
    turtle.setpos((0, -200))
    turtle.clear()
    turtle.left(90)
    turtle.pensize(PEN_SIZE)
    stack = deque()
    for c in axiom:
        if c == '0':
            turtle.pensize(4)
            if random.random() > 0.5:
                turtle.pencolor('green')
            elif random.random() > 0.5:
                turtle.pencolor('#00e100')
            else:
                turtle.pencolor('#70bf5d')
            turtle.forward(LINE_LENGTH)
            turtle.pencolor('black')
            turtle.pensize(PEN_SIZE)
        elif c == '1' or c == '3':
            turtle.forward(LINE_LENGTH)
        elif c == '2':
            if random.random() > 0.75:
                turtle.forward(LINE_LENGTH)
        elif c == '[':
            stack.appendleft((turtle.position(), turtle.heading(), PEN_SIZE))
            PEN_SIZE = PEN_SIZE * 0.7
            turtle.pensize(PEN_SIZE)
            turtle.left(ANGLE + random.randint(0, 10))
        elif c == ']':
            pos, heading, PEN_SIZE = stack.popleft()
            turtle.pensize(PEN_SIZE)
            turtle.penup()
            turtle.setpos(pos)
            turtle.setheading(heading)
            turtle.right(ANGLE + random.randint(-10, 10))
            turtle.pendown()

    turtle.hideturtle()
    turtle.done()


if __name__ == '__main__':
    main()
