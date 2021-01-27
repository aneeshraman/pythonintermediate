from math import pi


# Program to find area and perimeter of a triangle (accept height and base from the user)
def area(base, height):
    return f"Area of the triangle is {0.5 * base * height}"


def perimeter(side_a=None, side_b=None, side_c=None, two_equal_sides=None, unequal_side=None, three_equal_sides=None):
    type_ = None
    if side_a is not None and side_b is not None and side_c is not None:
        type_ = "scalene"

    elif two_equal_sides is not None and unequal_side is not None:
        type_ = "isosceles"

    elif three_equal_sides is not None:
        type_ = "equilateral"

    if type_ is "scalene":
        return f"Perimeter of the triangle is: {side_a + side_b + side_c}"

    elif type_ is "isosceles":
        return f"Perimeter of the triangle is: {(2 * two_equal_sides) + unequal_side}"

    elif type_ is "equilateral":
        return f"Perimeter of the triangle is: {3 * three_equal_sides}"

    if type_ is None:
        return Exception("Wrong input given.")


# Program to find surface area and volume of a cuboid.
def surface_area(length, breadth, height):
    try:
        return f"Surface area of the cuboid is: {2 * (length * breadth + breadth * height + length * height)}"
    except ValueError:
        return Exception("Wrong input")


# Program to find surface area and volume of a cylinder (pi = 3.14)
def surface_area_of_cylinder(height, radius):
    try:
        return f"The surface area of the cylinder is: {2 * radius * height}π or approximate value would " \
               f"be {2 * radius * height * pi}"

    except ValueError:
        return Exception("Wrong input")


# Program to find the area of perimeter of a circle.
def area_of_circle(radius):
    try:
        return f"The area of the circle is {radius ** 2}π or approximate value would be {pi * radius ** 2}"

    except ValueError:
        return Exception("Invalid input")


# Program to find the simple interest and the amount after accepting P, R, T.
def simple_interest(principle, rate, time):
    try:
        return f"The simple interest is {principle * rate * time / 100}"

    except ValueError:
        return Exception("Invalid input")


# Program to find the compound interest and the amount after accepting P, R, and T.
def compound_interest(principle, rate, time):
    try:
        return f"The compound interest is {principle * (1 + rate / 100) ** time}"

    except ValueError:
        return Exception("Invalid input.")
