from math import pi, sin, cos
from time import sleep
from threading import Thread


class Fractal:
    def __init__(self, canvas, depth, x=500, y=1000, length=250, angle=pi/2,
                 deviation=pi/4, decrease=0.7, time=0.0001):
        self.canvas = canvas
        self.x, self.y = x, y
        self.length = length
        self.angle = angle
        self.deviation = deviation
        self.decrease = decrease
        self.depth = depth
        self.time = time
        self.__draw_first_tree(self.x, self.y, self.length, self.angle,
                               self.deviation, self.decrease, self.depth, self.time)

    def __draw_first_tree(self, x, y, length, angle, deviation, decrease, depth, time):
        """ Draws part of the tree and passes the rest of the rendering in multi-threaded mode """
        x_1, y_1, x_2, y_2 = self.__calculating_coordinates(x, y, length, angle)
        self.canvas.create_line(x_1, y_1, x_2, y_2, fill='#ffffff')
        self.canvas.update()
        sleep(time)
        if depth > 1:
            new_length = length * decrease
            thread_1 = Thread(target=self.__draw_tree_to_right,
                              args=(x_2, y_2, new_length, angle - deviation + pi / 2,
                                    deviation, decrease, depth - 1, time,), daemon=True)
            thread_1.start()
            thread_2 = Thread(target=self.__draw_tree_to_left,
                              args=(x_2, y_2, new_length, angle - deviation,
                                    deviation, decrease, depth - 1, time), daemon=True)
            thread_2.start()

    def __draw_tree_to_right(self, x, y, length, angle, deviation, decrease, depth, time):
        """ Draws a tree from left to right """
        x_1, y_1, x_2, y_2 = self.__calculating_coordinates(x, y, length, angle)
        self.canvas.create_line(x_1, y_1, x_2, y_2, fill='#ffffff')
        self.canvas.update()
        sleep(time)
        if depth > 1:
            new_length = length * decrease
            self.__draw_tree_to_right(x_2, y_2, new_length, angle - deviation + pi / 2,
                                      deviation, decrease, depth - 1, time)
            self.__draw_tree_to_right(x_2, y_2, new_length, angle - deviation, deviation, decrease, depth - 1, time)

    def __draw_tree_to_left(self, x, y, length, angle, deviation, decrease, depth, time):
        """ Draws a tree from right to left """
        x_1, y_1, x_2, y_2 = self.__calculating_coordinates(x, y, length, angle)
        self.canvas.create_line(x_1, y_1, x_2, y_2, fill='#ffffff')
        self.canvas.update()
        sleep(time)
        if depth > 1:
            new_length = length * decrease
            self.__draw_tree_to_left(x_2, y_2, new_length, angle - deviation, deviation, decrease, depth - 1, time)
            self.__draw_tree_to_left(x_2, y_2, new_length, angle - deviation + pi / 2,
                                     deviation, decrease, depth - 1, time)

    @staticmethod
    def __calculating_coordinates(x, y, length, angle):
        """ Calculating coordinates for building a tree branch """
        return x, y, round(x + length * cos(angle)), round(y - length * sin(angle))
