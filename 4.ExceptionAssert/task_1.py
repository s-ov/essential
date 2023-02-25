# Выучите основные стандартные исключения, которые перечислены в данном уроке.
import math


def circle(radius_):
    circle_square = round((radius_ ** 2 * math.pi), 2)
    return f"Circle square {circle_square}"


while True:
    try:
        radius = float(input('Enter radius of circle: '))
        if radius <= 0:
            print("Radius must be greater then 0")
        else:
            break
    except ValueError:
        print("Value error")

print(circle(radius))


def cone(radius_, height_):
    cone_volume = round((radius_ ** 2 * math.pi * height_), 2)
    return f"Cone volume {cone_volume}"


while True:
    try:
        radius = float(input('Enter radius of cone base: '))
        if radius <= 0:
            print("Radius must be greater then 0")
        else:
            break
    except ValueError:
        print("Value error")
while True:
    try:
        height = float(input('Enter height of cone: '))
        if height <= 0:
            print("Height must be greater then 0")
        else:
            break
    except ValueError:
        print("Value error")

print(cone(radius, height))
