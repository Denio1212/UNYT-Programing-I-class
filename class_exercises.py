"""
Task 6 and after since I had issues with canvas earlier
"""

def decimal_value():
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    dec_value = numerator / denominator
    print(dec_value.__float__())


def area_of_circle():
    """
    Task 7
    """
    pi = 3.14159
    radius = float(input("Enter a radius: "))
    area = pi * radius * radius
    print(area)


def round_the_number():
    """
    Task 8
    """
    number = float(input("Enter a number: "))
    rounded_number = round(number)
    print("{0}, rounded off to the nearest int is {1}".format(number, rounded_number))

round_the_number()