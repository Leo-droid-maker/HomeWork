from time import sleep
import turtle


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        colors = ['red', 'yellow', 'green']
        if type(self.__color) is str:
            if self.__color in colors:

                window = turtle.Screen()
                window.setup(200, 500)
                window.bgcolor('blue')
                border = turtle.Turtle()
                border.hideturtle()
                border.color('gray')
                border.speed(0)
                border.up()
                border.goto(80, 200)
                border.begin_fill()
                border.down()
                border.goto(80, -200)
                border.goto(-80, -200)
                border.goto(-80, 200)
                border.goto(80, 200)
                border.end_fill()
                turtle.hideturtle()
                turtle.speed(0)
                turtle.penup()
                turtle.goto(0, 90)
                turtle.color('black')
                turtle.begin_fill()
                turtle.pendown()
                turtle.circle(45)
                turtle.end_fill()
                turtle.penup()
                turtle.goto(0, 0)
                turtle.color('black')
                turtle.begin_fill()
                turtle.pendown()
                turtle.circle(45)
                turtle.end_fill()
                turtle.penup()
                turtle.goto(0, -90)
                turtle.color('black')
                turtle.begin_fill()
                turtle.pendown()
                turtle.circle(45)
                turtle.end_fill()

                while True:
                    for color in range(len(colors)):
                        try:
                            turtle.color(colors[color + 1])
                            turtle.penup()
                            turtle.speed(0)
                            turtle.hideturtle()
                            if colors[color] == 'red':
                                turtle.color(colors[color])
                                turtle.goto(0, 90)
                                turtle.begin_fill()
                                turtle.pendown()
                                turtle.circle(45)
                                turtle.end_fill()
                                sleep(2)
                                turtle.penup()
                                turtle.goto(0, 90)
                                turtle.color('black')
                                turtle.begin_fill()
                                turtle.pendown()
                                turtle.circle(45)
                                turtle.end_fill()
                                continue
                            elif colors[color] == 'yellow':
                                turtle.color(colors[color])
                                turtle.goto(0, 0)
                                turtle.begin_fill()
                                turtle.pendown()
                                turtle.circle(45)
                                turtle.end_fill()
                                sleep(2)
                                turtle.penup()
                                turtle.goto(0, 0)
                                turtle.color('black')
                                turtle.begin_fill()
                                turtle.pendown()
                                turtle.circle(45)
                                turtle.end_fill()
                                continue
                            elif colors[color] == 'green':
                                turtle.color(colors[color])
                                turtle.goto(0, -90)
                                turtle.begin_fill()
                                turtle.pendown()
                                turtle.circle(45)
                                turtle.end_fill()
                                sleep(2)
                                turtle.penup()
                                turtle.goto(0, -90)
                                turtle.color('black')
                                turtle.begin_fill()
                                turtle.pendown()
                                turtle.circle(45)
                                turtle.end_fill()
                                continue
                        except IndexError:
                            colors.reverse()
                            continue

            else:
                print('There is no color...')

        else:
            print('Wrong argument')


a = TrafficLight('green')
a.running()
