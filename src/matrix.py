#!/usr/bin/env python

from six.moves import range

class Matrix:

    def __init__(self, iterator, start_x, start_y):
        self.matrix = self.setup_matrix(iterator, start_x, start_y)

    def setup_matrix(self, iterator, start_x, start_y):
        matrix = {}
        for x in range((start_x - (7 + iterator)) * 64, (iterator + start_x + 8) * 64):
            matrix[x] = {}
            for y in range((start_y - (7 + iterator)) * 64, (iterator + start_y + 8) * 64):
                matrix[x][y] = None
        return matrix

    def update(self, x, y, color):
        if self.exist_axis(x, y):
            self.matrix[x][y] = color

    def exist_axis(self, x, y):
        try:
            self.matrix[x][y]
        except IndexError:
            return False
        return True

    def get_color(self, x, y):
        if self.exist_axis(x, y):
            return self.matrix[x][y]

        return None
