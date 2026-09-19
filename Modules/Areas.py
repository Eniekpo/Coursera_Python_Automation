import math


def triangle(base, height):
    return base * height / 2  #[cite: 20]


def rectangle(base, height):
    return base * height  #[cite: 20]


def circle(radius):
    return math.pi * (radius**2)  #[cite: 20]

def square(side):
    return side * side  #[cite: 20]

def trapezoid(base1, base2, height):
    return (base1 + base2) * height / 2  #[cite: 20]

def donut(outer_radius, inner_radius):
    return math.pi * (outer_radius**2 - inner_radius**2)  #[cite: 20]   