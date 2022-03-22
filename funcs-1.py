# Lab 2 Functions
# Name: Joanna Chou
# Section: 07
import math

# 1)purpose statement:This function computes a given formula.
# signature:int int -> float
def do_math(x, y):
    ans1 = ((x ** 2) - ((3 / 5) * x * (y ** 2))) / (((2 * (x ** 2) * y) / 5) + 4)
    return ans1


# 2)purpose statement: This function computes the quadratic formula where the square root is positive.
# signature: int int int -> float
def quadratic_formula1(a, b, c):
    ans2 = (-b + (math.sqrt((b ** 2) - (4 * a * c)))) / (2 * a)
    return ans2


# 3)purpose statement: This function computes the quadratic formula where the square root is negative.
# signature: int int int -> float
def quadratic_formula2(a, b, c):
    ans3 = (-b - (math.sqrt((b ** 2) - (4 * a * c)))) / (2 * a)
    return ans3


# 4)purpose statement: This function computes the distance between two coordinate points.
# signature: int int int int -> int
def distance(x1, y1, x2, y2):
    ans4 = abs(x1 - x2) + abs(y1 - y2)
    return ans4


# 5)purpose statement: This function takes a number and returns False if the number is negative and True otherwise.
# signature: int -> bool
def is_positive(num):
    ans5 = num > 0
    return ans5


# 6)purpose statement: This function takes a number and returns True if the number is dividable by 7 and False otherwise.
# signature: int -> bool
def dividable_by_7(num):
    ans6 = num % 7 == 0
    return ans6