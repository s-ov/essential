import math


def calc_rect_square(length, width):
    return length * width


def calc_square(side):
    return side ** 2


def calc_round_square(radius):
    return 2 * math.pi * radius


def calc_tri_square(height, side):
    return 0.5 * height * side


def calc_cube_volume(edge):
    return edge ** 3


def calc_ball_volume(radius):
    return 4 / 3 * math.pi * radius ** 3