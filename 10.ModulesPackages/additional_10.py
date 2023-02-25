import geometry as g

while True:
    menu = input("Menu:\n1.Square area.\n2.Rectangle square.\n3.Round square.\n4.Triangle square.\n"
                 "5.Sphere volume.\n6.Cube volume\n7.Exit.\nChoose a number of issue: ")
    if menu == '1':
        side = input("Enter side: ")
        try:
            side = float(side)
            print(g.calc_square(side))
        except ValueError:
            print("Value error.")
    elif menu == '2':
        length = input("Enter length: ")
        width = input("Enter width: ")
        try:
            length = float(length)
            width = float(width)
            print(g.calc_rect_square(length, width))
        except ValueError:
            print("Value error.")
    elif menu == '3':
        radius = input("Enter radius: ")
        try:
            radius = float(radius)
            print(g.calc_round_square(radius))
        except ValueError:
            print("Value error.")
    elif menu == '4':
        height = input("Enter height: ")
        side = input("Enter side: ")
        try:
            height = float(height)
            side = float(side)
            print(g.calc_tri_square(height, side))
        except ValueError:
            print("Value error.")
    elif menu == '5':
        radius = input("Enter radius: ")
        try:
            radius = float(radius)
            print(g.calc_ball_volume(radius))
        except ValueError:
            print("Value error.")
    elif menu == '6':
        edge = input("Enter edge: ")
        try:
            edge = float(edge)
            print(g.calc_cube_volume(edge))
        except ValueError:
            print("Value error.")
    elif menu == '7':
        break
    else:
        print("incorrect input.")
