import math


def circle_computation():
    radius = (float(input("Enter the radius of a circle:\n")))

    try:
        diameter = 2 * radius
        print("This is the diameter of the circle:", '{0:.3f}'.format(diameter))
        circumference = 2.0 * math.pi * radius
        print("This is the circumference of the circle:", '{0:.3f}'.format(circumference))
        area = math.pi * radius * radius
        print("This is the area of the circle:", '{0:.3f}'.format(area))
    except ValueError:
        print("Sorry, this is not a valid input")
        quit()


circle_computation()  # completed
